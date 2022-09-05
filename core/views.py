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
# Create your views here.

class Rent(APIView):

    @transaction.atomic
    def post(self , request):
        customer = request.customer
        #create Loan object
        
        loan_object = LoanModel.objects.create(borrower = customer)

        book_objects = Basket.objects.filter(customer = customer).values('book_object__code')

        loan_object.save()
        
        for book_object in book_objects:

            code = book_object['book_object__code']

            book_object = BookObject.objects.get(code = code)

            loan_book = LoanBook.objects.create(loan = loan_object , book_object = book_object)

            loan_book.save()

        Basket.objects.filter(customer = customer).delete()

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

class Resend(APIView):
    pass

class QuickViewOfLoans(ListAPIView):
    pass

class LoanLogs(RetrieveAPIView):
    pass