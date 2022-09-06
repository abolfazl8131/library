import code
from codecs import BOM
from urllib import request
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, UpdateAPIView, RetrieveAPIView, DestroyAPIView, ListAPIView
from rest_framework.views import APIView
from bookbasket.basket import BookBasket
from book.models import BookObject
from customer.models import Customer
from core.models import Basket
from .serializers import BasketSerializer
from .models import *
from django.db import transaction
import uuid
from sub_view.loan_manager import LoanManager
from sub_view.book_object_manager import BOM_ 
# Create your views here.

class Rent(APIView):

    @transaction.atomic
    def post(self , request):
        customer = request.customer
        
        
        loan_manager = LoanManager()
        loan_object = loan_manager.create(customer)

        bom = BOM_()
        bom.save(loan_object , customer)

        return Response("your reservation has been saved!" , status=201)

       



class AddToBasket(APIView):
    
    serializer_class = BasketSerializer
    

    def post(self , format = None):
        data = self.request.data
        basket = BookBasket(BookObject,Basket,self.request.customer)
        
        basket.add(data['object'])
        serializer = self.serializer_class(data = basket.get() , many = True)
        serializer.is_valid()
        return JsonResponse({"basket":serializer.data})
        

class DeleteBasket(DestroyAPIView):
    
    def delete(self, request, *args, **kwargs):
        param = request.GET.get('object')
        basket = BookBasket(BookObject,Basket,request.customer)
        if param == None:
            basket.delete()
            return JsonResponse({"msg":"deleted your current basket"})
        
        basket.delete_obj(param)
        return JsonResponse({"msg":"your object has been deleted successfully!"})


class GetBasket(APIView):

    serializer_class = BasketSerializer

    def get(self , request):
        basket = BookBasket(BookObject,Basket,request.customer)
        serializer = self.serializer_class(data = basket.get() , many = True)
        serializer.is_valid()
        return JsonResponse({"basket":serializer.data})


class ReciveAPIView(APIView):
    def post(self , format = None):
        data = request.data
        loan_manager = LoanManager()
        loan_manager.delivered(data)
        return JsonResponse({"msg":"saved!"})


class EndRentAPIView(APIView):
    def post(self , format = None):
        data = request.data

        loan_manager = LoanManager()
        loan_manager.end(data)

        bom = BOM_()
        bom.availablity(data)
        return JsonResponse({"msg":"saved"})

 

class QuickViewOfLoans(ListAPIView):
    pass

class LoanLogs(RetrieveAPIView):
    pass