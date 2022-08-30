from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import Basket
from book.serializers import BookObjectGetSerializer , BookObjectSerializer

class BasketSerializer(serializers.ModelSerializer):
    book_object = BookObjectGetSerializer()
    class Meta:
        model = Basket
        fields = ['customer' , 'book_object' , 'date_submitted']
        extra_kwargs = {
            'customer': {'write_only': True}, 
        }

