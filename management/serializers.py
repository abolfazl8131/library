from dataclasses import fields
from django.http import JsonResponse
from rest_framework import serializers
from rest_framework.response import Response

from management.models import *
from django.contrib.auth import get_user_model
LibraryAdmin = get_user_model()

class SignUpAdminSerializer(serializers.ModelSerializer):

    class Meta:
        model = LibraryAdmin

        fields = ['ID',
        'first_name', 
        'last_name', 
        'birth_date',
        'email',
        'phone_number' ,
        'date_joined',
        'position']


        extra_kwargs = {
            'email': {'write_only': True},
            'phone_number': {'write_only': True},
            'date_joined': {'read_only' : True}
        }


class UpdateAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = LibraryAdmin
        fields = ['ID',
        'first_name', 
        'last_name', 
        'birth_date',
        'email',
        'phone_number' ,
        'position']


class GetAdminListSerializer(serializers.ModelSerializer):
    class Meta:
        model = LibraryAdmin
        fields = ['ID',
        'first_name', 
        'last_name', 
        'birth_date',
        'date_joined',
        'date_left',
        'email',
        'phone_number' ,
        'is_active',
        'left',
        'position']

