from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, UpdateAPIView, RetrieveAPIView, DestroyAPIView, ListAPIView
from rest_framework.permissions import *
from rest_framework.views import APIView
from .serializers import *
from .OTP import OTP
from .validators import SignUpValidator, IDCodeValidator
from .models import *

class SignUp(CreateAPIView):
    serializer_class = SignUpSerializer

    def post(self, request, *args, **kwargs):

            data = request.data
            validator = SignUpValidator(data)
            is_valid = validator.is_valid()
            if is_valid != True:
                return JsonResponse({"error" : is_valid} , 400)

            serializer = self.serializer_class(data=data)
            serializer.is_valid()
            serializer.save()
            return JsonResponse(serializer.data)





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
        return JsonResponse({"data" : otp})



class EnterAuthCode(APIView):
    serializer_class = GetCustomerSerializer

    def post(self , format=None):
        try:
            data = self.request.data
            customer = SignInCode.objects.get(code = data['code']).customer
        
            customer = self.serializer_class(customer)
            return JsonResponse({"user" : customer.data})
        except:
            return JsonResponse({"error":"your code in invalid! mybe expired or wrong!"})

