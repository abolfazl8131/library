from django.shortcuts import render

from validator.signup_validators import SignUpValidator

from validator.update_customer_validator import UpdateCustomerValidator

from validator.ID_unique_validator import IDCodeValidator

from django.http import JsonResponse
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *

# what master do with admin

class SignUpAdmin(APIView):

    def post(self , format = None):
        data = self.request.data
        validator = SignUpValidator(data)
        if not validator.is_valid() == True:

            return JsonResponse({"error" : is_valid})
        pass



class UpdateAdmin(APIView):
    pass

class DeleteAdmin(APIView):
    pass 

class DeActivateAdmin(APIView):
    pass

class ActivateAdmin(APIView):
    pass

