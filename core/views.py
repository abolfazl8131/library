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
# Create your views here.

class Rent(APIView):
    def post(self , request):
        pass


class AddToBasket(APIView):
    
    serializer_class = BasketSerializer
    permission_classes = []

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

class Resend(APIView):
    pass

class QuickViewOfLoans(ListAPIView):
    pass

class LoanLogs(RetrieveAPIView):
    pass