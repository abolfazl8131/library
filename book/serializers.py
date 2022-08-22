from dataclasses import field
from statistics import mode
from rest_framework import serializers
from .models import *

class BookGenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookGenre
        fields = ['genre']



class BookClassSerializer(serializers.ModelSerializer):

    genre = serializers.SlugRelatedField(queryset = BookGenre.objects.all() , slug_field='genre')
    
    class Meta:
        model = BookClass
        fields = ['name' , 'genre' , 'authors']
        




class BookObjectSerializer(serializers.ModelSerializer):
    book_class = serializers.SlugRelatedField(queryset = BookClass.objects.all() , slug_field='name')
    class Meta:
        model = BookObject
        fields = ['code' , 'date_published' , 'published_no' , 'book_class']

