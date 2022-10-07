
from requests import request
from rest_framework.response import Response
from rest_framework import status
from validator.admin_query_validator import AdminQueryValidator
from validator.signup_validators import SignUpValidator
from rest_framework.generics import UpdateAPIView, DestroyAPIView, ListAPIView,CreateAPIView,RetrieveAPIView
from permissions.is_master import IsMaster
from .serializers import SignUpAdminSerializer , UpdateAdminSerializer , GetAdminListSerializer
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import LibraryAdmin
from validator.update_admin_validator import UpdateAdminValidator 
from shared_queries.get_all_objects import GetManagementObjects
from permissions.is_active import IsActive
from permissions.is_clerk import IsClerk
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.conf import settings
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from shared_queries.advaned_data_query import AdvancedDataQuery
from validator.customer_query_validator import CustomerQueryValidator
from company.serializers import CompanySerializer
from django.core import serializers as generic_serializer
from shared_queries.lib_admin_middleware import find_library_admin
#LibraryAdmin = get_user_model()
# what master do with admin

permissions = [IsActive , IsMaster]

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


'''
    we get the request of develop a new company (library) and register the admin for it with master value,,,

'''
class RegisterMasterOfCompany(CreateAPIView):
    serializer_class = SignUpAdminSerializer

    def post(self , format = None):

        data = self.request.data
        
        serializer = self.serializer_class(data = data)
        
        serializer.is_valid(raise_exception= True)

        serializer.save()

        return JsonResponse({"data": serializer.data})



#master admin registeres admin
class SignUpAdmin(CreateAPIView):
    serializer_class = SignUpAdminSerializer
    permission_classes = permissions

    def post(self , format = None):
        data = self.request.data

        validator = SignUpValidator(data)
        validator.run()
        validator.model = LibraryAdmin
        validator.is_valid()
        
        master = find_library_admin(self.request.user.id)
        data['company'] = master.company.id
        serializer = self.serializer_class(data = data)
        
        serializer.is_valid(raise_exception=True)

        serializer.save()

        return JsonResponse({"data": serializer.data})



class UpdateAdmin(UpdateAPIView):
    permission_classes = permissions
    #add other permission
    serializer_class = UpdateAdminSerializer

    def get_object(self , **kwargs):
        lib_admin = find_library_admin(self.request.user.id)
        return LibraryAdmin.objects.get(id=lib_admin.company.id)

    def patch(self , request):
        data = request.data  
        serializer = self.serializer_class(self.get_object(),data = data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
       
        return JsonResponse({"data": serializer.data})

class DeleteAdmin(DestroyAPIView):
    permission_classes = permissions
    #add other permission
    def get_object(self , **kwargs):
        
        
        return LibraryAdmin.objects.get(**kwargs)

    def delete(self, request):
        ID = request.GET.get('ID')
        lib_master = find_library_admin(request.user.id)
        obj = self.get_object(ID = ID , company = lib_master.company)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class DeActivateAdmin(APIView):
    permission_classes = permissions
    #add other permission
    def get_object(self , **kwargs):
        
        query = GetObjects(LibraryAdmin , find_library_admin(self.request.user.id).company)
        query.run()
        return query.get_object(**kwargs)


    def post(self , request):
        ID = request.GET.get('ID')
        
        obj = self.get_object(ID = ID)
        obj.deactivate()
        obj.save()
        return JsonResponse({"data":obj.is_active} , status = 200)
    


class ActivateAdmin(APIView):
    permission_classes = permissions
    #add other permission
    def get_object(self , **kwargs):
        
        query = GetObjects(LibraryAdmin , find_library_admin(self.request.user.id).company)
        query.run()
        return query.get_object(**kwargs)

    def post(self , request):
        ID = request.GET.get('ID')
        
        obj = self.get_object(ID = ID)
        obj.activate()
        obj.save()
        return JsonResponse({"data":obj.is_active} , status = 200)

class LeaveAdmin(APIView):
    permission_classes = permissions
    #add other permission
    def get_object(self , **kwargs):
        lib_master = find_library_admin(self.request.user.id)
        query = GetObjects(LibraryAdmin , lib_master.company)
        query.run()
        return query.get_object(**kwargs)

    def post(self, request):
        ID = request.GET.get('ID')
       
        obj = self.get_object(ID = ID)
        obj.leave()
        obj.save()
        return JsonResponse({'data':obj.left})

        

#########################################################################################################################################################

# the methods will be declared on shared_views module!


class OverallViewOnAdmins(ListAPIView):
    serializer_class = GetAdminListSerializer
    permission_classes = permissions

  
    def get_queryset(self):
        lib_master = find_library_admin(self.request.user.id)
        query = GetObjects(LibraryAdmin , lib_master.company)
        query.run()
        return query.get_all()

    def get_object(self , **kwargs):
        lib_master = find_library_admin(self.request.user.id)
        query = GetObjects(LibraryAdmin , lib_master.company)
        query.run()
        return query.get_object(**kwargs)

    @method_decorator(cache_page(CACHE_TTL))
    def get(self, request,*args,**kwargs):

        data = request.GET.get

        ID = data("ID")

        if not ID == "":
           
            obj = self.get_object(ID = ID )  
           
            serializer = self.serializer_class(obj , many=False) 
            
            return JsonResponse({"admin":serializer.data})

        query = self.get_queryset()

        serializer = self.serializer_class(query , many = True)
        
        return JsonResponse({"data":serializer.data})


class FilterAdmins(ListAPIView):
    serializer_class = GetAdminListSerializer
    permission_classes = permissions

    def get_queryset(self , **kwargs):

        qs = AdvancedDataQuery(LibraryAdmin)
        qs.run()
        return qs.data_query(**kwargs , company = find_library_admin(self.request.user.id).company)
    
    @method_decorator(cache_page(CACHE_TTL))
    def get(self, request):

        query_params = request.GET

        params = dict(query_params.lists())

        print(params.items())

        for k,v in params.items():
            params[k] = v[0]
            
        validator = AdminQueryValidator(params)
        validator.run()

        validator.is_valid()
    
        qs = self.get_queryset(**params)

        serializer = self.serializer_class(qs , many = True)

        return JsonResponse({"data":serializer.data})
#################################################################################################################3
from customer.serializers import *

class OverallViewOnCustomers(ListAPIView):
    permission_classes = permissions

    serializer_class = GetCustomerSerializer

    def get_queryset(self):
        lib_master = find_library_admin(self.request.user.id)
        qs = GetObjects(Customer,lib_master.company)
        qs.run()
        qs = qs.get_all()
        return qs

    def get_object(self , **kwargs):
        lib_master = find_library_admin(self.request.user.id)
        obj = GetObjects(Customer,lib_master.company)
        obj.run()
        obj = obj.get_object(**kwargs)
        return obj

    @method_decorator(cache_page(CACHE_TTL))
    def get(self , request):

        data = request.GET.get

        customer_ID = data("ID")

        if customer_ID:
            lib_master = find_library_admin(request.user.id)
            obj = self.get_object(ID = customer_ID , company = lib_master.company)  
           
            serializer = self.serializer_class(obj , many=False) 
            
            return JsonResponse({"customer":serializer.data})

        query = self.get_queryset()

        serializer = self.serializer_class(query , many = True)
        
        return JsonResponse({"data":serializer.data})


        

class CustomerFilter(APIView):
    permission_classes = permissions

    serializer_class = GetCustomerSerializer

    def get_queryset(self , **kwargs):

        qs = AdvancedDataQuery(Customer)
        qs.run()
        kwargs['company'] = find_library_admin(self.request.user.id)
        return qs.data_query(**kwargs)

    @method_decorator(cache_page(CACHE_TTL))
    def get(self , request):
        
        query_params = request.GET

        params = dict(query_params.lists())

        for k,v in params.items():

            params[k] = v[0]
        
        validator = CustomerQueryValidator(params)

        validator.run()

        validator.is_valid()

        qs = self.get_queryset(**params)

        serializer = self.serializer_class(qs , many = True)

        return JsonResponse({"data":serializer.data})
###############################################################################################################################

class GetProfileAPIView(APIView):
    permission_classes = [IsMaster | IsClerk]

    
    def get(self , request):
        try:
            user = request.user

            library_admin = LibraryAdmin.objects.get(id = user.id)

            return JsonResponse({"first_name":library_admin.first_name , 
                    "last_name":library_admin.last_name ,
                    "position":library_admin.position, "company_name":library_admin.company.name})
                    
        except Exception as e:
            raise e


class MyCompanyAPIView(RetrieveAPIView):
    pass