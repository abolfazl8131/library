from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, UpdateAPIView, RetrieveAPIView, DestroyAPIView, ListAPIView
from rest_framework.permissions import *
from rest_framework.views import APIView
from customer.serializers import *
from .OTP import OTP

from customer.models import *

from validator.signup_validators import SignUpValidator

from validator.update_customer_validator import UpdateCustomerValidator

from validator.ID_unique_validator import IDCodeValidator

from django.db import transaction
from .jwt import JsonWebToken
from django.utils.decorators import decorator_from_middleware
from middlewars.jwt_middleware import JWTMiddleWare



class EnterID(APIView):

   
    def post(self, format = None):

        data = self.request.data

        validator = IDCodeValidator(data)

        is_valid = validator.is_valid()

        if not is_valid == True:

            return JsonResponse({"error" : is_valid} , status=400)

        sending_type = data['type'] | 1

        otp_obj = OTP(data , sending_type)
        otp = otp_obj.choose()


        otp_obj = OTP(data , sending_type)

        otp = otp_obj.choose()


        return JsonResponse({"data" : otp})

import base64

class EnterAuthCode(APIView):

    serializer_class = GetCustomerSerializer

   
    def post(self , format=None):

        try:
            data = self.request.data

            encoded_otp = base64.b64encode(bytes(data['code'], 'utf-8'))
            
            customer = SignInCode.objects.get(code = encoded_otp).customer
        
            customer = self.serializer_class(customer).data

            jwt = JsonWebToken()
            
            jwt = jwt.sign(customer)

            return JsonResponse({"token" : jwt})

        except Exception as e:
            print(e)
            return JsonResponse({"error":"your code in invalid! mybe expired or wrong!"} , status = 401)




 

