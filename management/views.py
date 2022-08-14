from functools import partial
from rest_framework.response import Response
from rest_framework import status
from wsgiref.validate import validator
from django.shortcuts import render
from django.http import Http404
from validator.signup_validators import SignUpValidator
from rest_framework.generics import CreateAPIView, UpdateAPIView, RetrieveAPIView, DestroyAPIView, ListAPIView
from validator.update_customer_validator import UpdateCustomerValidator
from permissions.is_master import *
from validator.ID_unique_validator import IDCodeValidator
from .serializers import *
from django.http import JsonResponse
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from validator.update_admin_validator import *
from shared_queries.get_all_objects import *
from permissions.is_active import *
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.conf import settings
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from django.contrib.auth import get_user_model
LibraryAdmin = get_user_model()
# what master do with admin

permissions = [IsActive , IsMaster]

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)

class SignUpAdmin(APIView):
    serializer_class = SignUpAdminSerializer
    permission_classes = permissions

    def post(self , format = None):
        data = self.request.data
        validator = SignUpValidator(data)
        validator.model = LibraryAdmin
        is_valid = validator.is_valid()

        if not is_valid == True:

            return JsonResponse({"error" : is_valid} , status = 400)

        serializer_data = {

            "admin_ID" : data["ID"] , 
            "admin_first_name" : data['first_name'] ,
            "admin_last_name": data['last_name'] , 
            "admin_email":data['email'] , 
            "admin_birth_date":data['birth_date'],
            "admin_phone_number":data['phone_number'] , 
            "admin_position":data['position']

        }

        serializer = self.serializer_class(data = serializer_data)

        serializer.is_valid(raise_exception = True)

        serializer.save()

        return JsonResponse({"data": serializer.data})



class UpdateAdmin(UpdateAPIView):
    permission_classes = permissions
    serializer_class = UpdateAdminSerializer

    def get_object(self):
        try:
            _object = LibraryAdmin.objects.get(admin_ID = self.request.GET.get('ID'))
            return _object
        except:
            raise Http404

    def patch(self , request):
        data = request.data
        validator = UpdateAdminValidator(data)
        is_valid = validator.is_valid()
        
        if not is_valid == True:
            return JsonResponse({"error": is_valid} , status = 400)
        serializer_data = {

            "admin_ID" : data["ID"] , 
            "admin_first_name" : data['first_name'] ,
            "admin_last_name": data['last_name'] , 
            "admin_email":data['email'] , 
            "admin_birth_date":data['birth_date'],
            "admin_phone_number":data['phone_number'] , 
            "admin_position":data['position']

        }

        serializer = self.serializer_class(self.get_object(),data = serializer_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
       
        return JsonResponse({"data": serializer.data})

class DeleteAdmin(DestroyAPIView):
    permission_classes = permissions

    def get_object(self):
        
        try:
            _object = LibraryAdmin.objects.get(admin_ID = self.request.GET.get('ID'))
            return _object
        except:
            raise Http404

    def delete(self, request):
        obj = self.get_object()
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class DeActivateAdmin(APIView):
    permission_classes = permissions

    def get_object(self):
        
        try:
            _object = LibraryAdmin.objects.get(admin_ID = self.request.GET.get('ID'))
            return _object
        except:
            raise Http404

    def post(self , request):
        obj = self.get_object()
        obj.admin_is_active = False
        obj.save()
        return JsonResponse({"data":obj.admin_is_active} , status = 200)
    


class ActivateAdmin(APIView):
    permission_classes = permissions

    def get_object(self):
        
        try:
            _object = LibraryAdmin.objects.get(admin_ID = self.request.GET.get('ID'))
            return _object
        except:
            raise Http404

    def post(self , request):
        obj = self.get_object()
        obj.admin_is_active = True
        obj.save()
        return JsonResponse({"data":obj.admin_is_active} , status = 200)

class LeaveAdmin(APIView):
    permission_classes = permissions

    def get_object(self , ID):

        obj = LibraryAdmin.objects.get(admin_ID = ID)
        return obj

    def post(self, request):
        obj = self.get_object(request.GET.get('ID'))
        obj.leave()
        obj.save()
        return JsonResponse({'data':obj.admin_left})

        

#########################################################################################################################################################

# the methods will be declared on shared_views module!


class OverallViewOnAdmins(RetrieveAPIView):
    serializer_class = GetAdminListSerializer
    ppermission_classes = permissions

  
    def get_queryset(self):
        query = GetAllObjects(LibraryAdmin)
        
        return query.get_all()

    @method_decorator(cache_page(CACHE_TTL))
    def get(self, request,*args,**kwargs):
        query = self.get_queryset()
        serializer = self.serializer_class(query , many = True)
        return JsonResponse({"data":serializer.data})


class OverallViewOnCustomers():
    pass

class OverallViewOnBooks():
    pass

class OverallViewOnLoans():
    pass