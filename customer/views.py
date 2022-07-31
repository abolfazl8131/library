from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, UpdateAPIView, RetrieveAPIView, DestroyAPIView, ListAPIView
from rest_framework.permissions import *
from rest_framework.views import APIView
from customer.serializers import SignUpSerializer
from .validators import SignUpValidator

class SignUp(CreateAPIView):
    serializer_class = SignUpSerializer

    def create(self, request, *args, **kwargs):

            data = request.data
            validator = SignUpValidator(data)
            is_valid = validator.is_valid()
            if is_valid != True:
                return JsonResponse({"error" : is_valid})

            serializer = self.serializer_class(data=data)
            serializer.is_valid()
            serializer.save()
            return JsonResponse(serializer.data)





class Auth(APIView):
    pass
