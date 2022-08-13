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

        fields = ['admin_ID',
        'admin_first_name', 
        'admin_last_name', 
        'admin_birth_date',
        'admin_email',
        'admin_phone_number' ,
        'admin_date_joined',
        'admin_position']


        extra_kwargs = {
            'email': {'write_only': True},
            'phone_number': {'write_only': True},
            'date_joined': {'read_only' : True}
        }


class UpdateAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = LibraryAdmin
        fields = ['admin_ID',
        'admin_first_name', 
        'admin_last_name', 
        'admin_birth_date',
        'admin_email',
        'admin_phone_number' ,
        'admin_position']