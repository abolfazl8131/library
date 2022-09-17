from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import Basket , LoanModel , LoanBook
from book.serializers import BookObjectGetSerializer , BookObjectSerializer
from customer.serializers import GetCustomerSerializer

class BasketSerializer(serializers.ModelSerializer):
    book_object = BookObjectGetSerializer()
    class Meta:
        model = Basket
        fields = ['customer' , 'book_object' , 'date_submitted']
        extra_kwargs = {
            'customer': {'write_only': True}, 
        }


class RentListSerializer(serializers.ModelSerializer):
    borrower = GetCustomerSerializer()
    class Meta:
        model = LoanModel
        fields = '__all__'



class RentObjectSerializer(serializers.ModelSerializer):
    loan = RentListSerializer()
    book_object = BookObjectGetSerializer()
    class Meta:
        model = LoanBook
        fields = ['book_object' , 'loan']