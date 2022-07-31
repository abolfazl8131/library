from django.http import JsonResponse
from rest_framework import serializers
from rest_framework.response import Response

from customer.models import Customer



class SignUpSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = ['ID','first_name', 'last_name', 'birth_date','email','phone_number']

