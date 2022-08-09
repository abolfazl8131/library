from django.shortcuts import render
from validator.validators import *
from django.http import JsonResponse
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *

# what master do with admin

class SignUpAdmin(APIView):
    pass

class UpdateAdmin(APIView):
    pass

class DeleteAdmin(APIView):
    pass 

class DeActivateAdmin(APIView):
    pass

class ActivateAdmin(APIView):
    pass

