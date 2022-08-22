from ast import Pass
from binhex import LINELEN
from operator import ge
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from validator.book.book_validator import *
from .models import BookGenre
from rest_framework.generics import CreateAPIView, UpdateAPIView, RetrieveAPIView, DestroyAPIView, ListAPIView
from .serializers import *
from shared_queries.get_all_objects import *
from shared_queries.advaned_data_query import AdvancedDataQuery
# Create your views here.

class GenreRegister(APIView):

    serializer_class = BookGenreSerializer

    def post(self , format = None):
        
        data = self.request.data
        genre = data['genre']
        validator = BookGenreVlidator(BookGenre)
        is_valid = validator.isvalid(genre)
        if not is_valid == True:
            return JsonResponse({"error":is_valid})
        serializer = self.serializer_class(data = data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        print(serializer.data)
        return JsonResponse({"data":serializer.data})



class GenreFilter(ListAPIView):
    serializer_class = BookGenreSerializer
    queryset = BookGenre.objects.all()
    lookup_field = 'genre'




class DeleteGenre(DestroyAPIView):
    query_class = AdvancedDataQuery(BookGenre)

    def get_queryset(self , **kwargs):
        qs = self.query_class.data_query(**kwargs)
        return qs

    def delete(self , request):
        genre = request.GET.get('genre')
        qs = self.get_queryset(genre = genre)
        qs.delete()
        return JsonResponse({"msg":"deleted!"})
        
###############################################################################################################################################

class ClassRegister(APIView):

    serializer_class = BookClassSerializer

    def post(self , format = None):
        
        data = self.request.data

        validator = BookClassValidator(BookClass , BookGenre)

        is_valid = validator.isvalid(data['name'] , data['genre'])

        if not is_valid == True:

            return JsonResponse({"error":is_valid})

        serializer = self.serializer_class(data = data)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        return JsonResponse({"data":serializer.data})



class ClassFilter(ListAPIView):
    serializer_class = BookClassSerializer
    queryset = BookClass.objects.all()
    

   


class ClassDelete(DestroyAPIView):

    query_class = AdvancedDataQuery(BookClass)

    def get_queryset(self , **kwargs):
        qs = self.query_class.data_query(**kwargs)
        return qs

    def delete(self , request):
        name = request.GET.get('name')
        qs = self.get_queryset(name = name)
        qs.delete()
        return JsonResponse({"msg":"deleted!"})

##########################################################################################################################3

class ObjectRegister(APIView):
    serializer_class = BookObjectSerializer

    def post(self , format = None):
        
        data = self.request.data

        validator = BookObjectValidator(BookObject , BookClass)

        is_valid = validator.isvalid(data['code'] , data['book_class'] , data['date_published'] , data['published_no'])

        if not is_valid == True:

            return JsonResponse({"error":is_valid})

        serializer = self.serializer_class(data = data)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        return JsonResponse({"data":serializer.data})


class ObjectFilter(ListAPIView):

    serializer_class = BookObjectSerializer
    queryset = BookObject.objects.all()
    

   


