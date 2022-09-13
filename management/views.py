import re
from rest_framework.response import Response
from rest_framework import status
from validator.admin_query_validator import AdminQueryValidator
from validator.signup_validators import SignUpValidator
from rest_framework.generics import UpdateAPIView, DestroyAPIView, ListAPIView
from permissions.is_master import IsMaster
from .serializers import SignUpAdminSerializer , UpdateAdminSerializer , GetAdminListSerializer
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import LibraryAdmin
from validator.update_admin_validator import UpdateAdminValidator 
from shared_queries.get_all_objects import GetObjects
from permissions.is_active import IsActive
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.conf import settings
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from shared_queries.advaned_data_query import AdvancedDataQuery
from validator.customer_query_validator import CustomerQueryValidator
from django.contrib.auth import get_user_model

#LibraryAdmin = get_user_model()
# what master do with admin

permissions = (IsActive , IsMaster)

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)

class SignUpAdmin(APIView):
    serializer_class = SignUpAdminSerializer
    #permission_classes = permissions

    def post(self , format = None):
        data = self.request.data
        validator = SignUpValidator(data)
        validator.run()
        validator.model = LibraryAdmin
        validator.is_valid()
        serializer = self.serializer_class(data = data)

        serializer.is_valid()

        serializer.save()

        return JsonResponse({"data": serializer.data})



class UpdateAdmin(UpdateAPIView):
    permission_classes = permissions
    serializer_class = UpdateAdminSerializer

    def get_object(self , **kwargs):
        query = GetObjects(LibraryAdmin)
        query.run()
        return query.get_object(**kwargs)

    def patch(self , request):
        data = request.data
        ID = request.GET.get('ID')
        validator = UpdateAdminValidator(data)
        validator.run()
        validator.is_valid()
        serializer = self.serializer_class(self.get_object(ID = ID),data = data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
       
        return JsonResponse({"data": serializer.data})

class DeleteAdmin(DestroyAPIView):
    permission_classes = permissions

    def get_object(self , **kwargs):
        
        query = GetObjects(LibraryAdmin)
        query.run()
        return query.get_object(**kwargs)


    def delete(self, request):
        ID = request.GET.get('ID')
        obj = self.get_object(ID = ID)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class DeActivateAdmin(APIView):
    permission_classes = permissions

    def get_object(self , **kwargs):
        
        query = GetObjects(LibraryAdmin)
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

    def get_object(self , **kwargs):
        
        query = GetObjects(LibraryAdmin)
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

    def get_object(self , **kwargs):

        query = GetObjects(LibraryAdmin)
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

        query = GetObjects(LibraryAdmin)
        query.run()
        return query.get_all()

    def get_object(self , **kwargs):

        query = GetObjects(LibraryAdmin)
        query.run()
        return query.get_object(**kwargs)

    @method_decorator(cache_page(CACHE_TTL))
    def get(self, request,*args,**kwargs):

        data = request.GET.get

        ID = data("ID")

        if not ID == "":

            obj = self.get_object(ID = ID)  
           
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
        return qs.data_query(**kwargs)
    
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

from customer.serializers import *

class OverallViewOnCustomers(APIView):
    permission_classes = permissions

    serializer_class = GetCustomerSerializer

    def get_queryset(self):
        qs = GetObjects(Customer)
        qs.run()
        qs = qs.get_all()
        return qs

    def get_object(self , **kwargs):
        obj = GetObjects(Customer)
        obj.run()
        obj = obj.get_object(**kwargs)
        return obj

    @method_decorator(cache_page(CACHE_TTL))
    def get(self , request):

        data = request.GET.get

        customer_ID = data("ID")

        if not customer_ID == "":

            obj = self.get_object(ID = customer_ID)  
           
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


class GetProfileAPIView(APIView):
    def get(self , request):
        print(request.user)
        
        return JsonResponse({"first_name":request.library_admin.first_name , 
        "last_name":request.library_admin.last_name ,
         "position": request.library_admin.position })