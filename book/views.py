from ast import Pass
from operator import ge
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from validator.book.book_validator import BookVlidator
from .models import BookGenre
from rest_framework.generics import CreateAPIView, UpdateAPIView, RetrieveAPIView, DestroyAPIView, ListAPIView
from .serializers import *
from shared_queries.get_all_objects import *
# Create your views here.

class GenreRegister(APIView):

    serializer_class = BookGenreSerializer

    def post(self , format = None):
        
        data = self.request.data
        genre = data['genre']
        validator = BookVlidator(BookGenre)
        is_valid = validator.genre_isvalid(genre)
        if not is_valid == True:
            return JsonResponse({"error":is_valid})
        serializer = self.serializer_class(data = data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        print(serializer.data)
        return JsonResponse({"data":serializer.data})

class GenreFilter(ListAPIView):
    serializer_class = BookGenreSerializer
    query_class = GetObjects(BookGenre)

    def get_queryset(self):
        
        return self.query_class.get_all()

    def get_object(self , **kwargs):
        return self.query_class.get_object(**kwargs)


    def get(self , request):
        params = request.GET.get('genre')
        if params == "":
            qs = self.get_queryset()
            serializer = self.serializer_class(qs , many = True)
            return Response(serializer.data)
        
        obj = self.get_object(genre = params)
        
        serializer = self.serializer_class(obj)
        return JsonResponse({"data":serializer.data})


class ClassRegister():
    pass

class ObjectRegister():
    pass

