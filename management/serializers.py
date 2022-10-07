
from rest_framework import serializers
from company.models import Company

from management.models import LibraryAdmin

#LibraryAdmin = get_user_model()

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
        'position','company']


        extra_kwargs = {
            'email': {'write_only': True},
            'phone_number': {'write_only': True},
            'date_joined': {'read_only' : True},
            #'company':{'read_only':True}
        }


class UpdateAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = LibraryAdmin
        fields = ['ID','company',
        'first_name', 
        'last_name', 
        'birth_date',
        'email',
        'phone_number']

        extra_kwargs = {
            'ID': {'read_only': True},
            'company':{'read_only':True}
        }


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
        'position','company']

