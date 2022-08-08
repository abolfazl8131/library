from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, UpdateAPIView, RetrieveAPIView, DestroyAPIView, ListAPIView
from rest_framework.permissions import *
from rest_framework.views import APIView
from .serializers import *
from .OTP import OTP
<<<<<<< HEAD
from .validators import SignUpValidator, IDCodeValidator
from .models import *
=======
from .validators import SignUpValidator, IDCodeValidator , UpdateCustomerValidator
from .models import *
from django.db import transaction
from .jwt import JsonWebToken
from django.utils.decorators import decorator_from_middleware
from customer.middlewars.jwt_middleware import JWTMiddleWare
>>>>>>> jwt

class SignUp(CreateAPIView):
    serializer_class = SignUpSerializer

    @transaction.atomic()
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
<<<<<<< HEAD
        otp_obj = OTP(data , sending_type)
        otp = otp_obj.choose()
=======

        otp_obj = OTP(data , sending_type)

        otp = otp_obj.choose()

>>>>>>> jwt
        return JsonResponse({"data" : otp})



class EnterAuthCode(APIView):
<<<<<<< HEAD
    serializer_class = GetCustomerSerializer

    def post(self , format=None):
        try:
            data = self.request.data
            customer = SignInCode.objects.get(code = data['code']).customer
        
            customer = self.serializer_class(customer)
            return JsonResponse({"user" : customer.data})
        except:
            return JsonResponse({"error":"your code in invalid! mybe expired or wrong!"})
=======
>>>>>>> jwt

    serializer_class = GetCustomerSerializer

  
    def post(self , format=None):

        try:
            data = self.request.data

            customer = SignInCode.objects.get(code = data['code']).customer
        
            customer = self.serializer_class(customer).data

            jwt = JsonWebToken()
            
            jwt = jwt.sign(customer)

            return JsonResponse({"token" : jwt})

        except Exception as e:
            
            return JsonResponse({"error":"your code in invalid! mybe expired or wrong!"})

 


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

    def get_queryset(self):
        ID = self.request.customer.ID

        customer = Customer.objects.get(ID = ID)

        return customer

    def patch(self , request):
        data = request.data
        validator = UpdateCustomerValidator(data)
        is_valid = validator.is_valid()

        if not is_valid == True:

            return JsonResponse({"error" : is_valid} , status=400)
        
        serializer = self.serializer_class(self.get_queryset(),data = data , partial = True)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return JsonResponse(serializer.data , status = 201)
