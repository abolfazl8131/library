from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, UpdateAPIView, RetrieveAPIView, DestroyAPIView, ListAPIView
from rest_framework.permissions import *
from rest_framework.views import APIView
from customer.serializers import SignUpSerializer
from .OTP import OTP
from .validators import SignUpValidator, IDCodeValidator


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
        otp = OTP(data , sending_type)
        otp.choose()
        return JsonResponse({"data" : "we have sent message"})



class EnterAuthCode(APIView):
    pass

