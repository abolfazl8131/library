from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, UpdateAPIView, RetrieveAPIView, DestroyAPIView, ListAPIView
from rest_framework.permissions import *
from rest_framework.views import APIView
from .serializers import *
from authentication.OTP import OTP

from .models import *

from shared_queries.get_all_objects import GetObjects
from validator.signup_validators import SignUpValidator

from validator.update_customer_validator import UpdateCustomerValidator

from validator.ID_unique_validator import IDCodeValidator

from .models import *
from django.db import transaction
from authentication.jwt import JsonWebToken
from django.utils.decorators import decorator_from_middleware
from middlewars.jwt_middleware import JWTMiddleWare


class SignUp(CreateAPIView):
    serializer_class = SignUpSerializer

    @transaction.atomic()
    def post(self, request, *args, **kwargs):

            data = request.data
            validator = SignUpValidator(data)
            validator.start()
            validator.model = Customer
            is_valid = validator.is_valid()
            if is_valid != True:
                return JsonResponse({"error" : is_valid} , status = 400)

            serializer = self.serializer_class(data=data)
            serializer.is_valid()
            serializer.save()
            return JsonResponse(serializer.data)





class GetProfile(APIView):
    permission_class = []

    def get(self, request):

        
        return JsonResponse({
                'ID':request.customer.ID , 
                'firstname':request.customer.first_name , 
                'lastname':request.customer.last_name,
                'email':request.customer.email, 
                'phone':request.customer.phone_number,
                'birthdate':request.customer.birth_date,
                'date joined':request.customer.date_joined,})


class UpdateProfile(UpdateAPIView):
    serializer_class =  UpdateCustomerSerializer
    permission_class = []

    def get_queryset(self , **kwargs):
        query = GetObjects(Customer)
        query.start()
        return query.get_object(**kwargs)


    def patch(self , request):
        data = request.data
        ID = self.request.customer.ID
        validator = UpdateCustomerValidator(data)
        validator.start()
        is_valid = validator.is_valid()

        if not is_valid == True:

            return JsonResponse({"error" : is_valid} , status=400)
        
        serializer = self.serializer_class(self.get_queryset(ID = ID),data = data , partial = True)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return JsonResponse(serializer.data , status = 201)

