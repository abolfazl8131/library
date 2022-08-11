from django.shortcuts import render

from validator.signup_validators import SignUpValidator

from validator.update_customer_validator import UpdateCustomerValidator

from validator.ID_unique_validator import IDCodeValidator
from .serializers import *
from django.http import JsonResponse
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from django.contrib.auth import get_user_model
LibraryAdmin = get_user_model()
# what master do with admin

class SignUpAdmin(APIView):
    serializer_class = SignUpAdminSerializer

    def post(self , format = None):
        data = self.request.data
        validator = SignUpValidator(data)
        validator.model = LibraryAdmin
        is_valid = validator.is_valid()

        if not is_valid == True:

            return JsonResponse({"error" : is_valid} , status = 400)

        serializer_data = {"admin_ID" : data["ID"] , 
        "admin_first_name" : data['first_name'] ,
        "admin_last_name": data['last_name'] , 
        "admin_email":data['email'] , 
        "admin_birth_date":data['birth_date'],
        "admin_phone_number":data['phone_number'] , 
        "admin_position":data['position']}

        serializer = self.serializer_class(data = serializer_data)

        serializer.is_valid(raise_exception = True)

        serializer.save()

        return JsonResponse({"data": serializer.data})



class UpdateAdmin(APIView):
    pass

class DeleteAdmin(APIView):
    pass 

class DeActivateAdmin(APIView):
    pass

class ActivateAdmin(APIView):
    pass

