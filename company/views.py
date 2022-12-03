from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CompanySerializer
from .models import Company
from rest_framework.generics import DestroyAPIView, ListAPIView , CreateAPIView,UpdateAPIView
# Create your views here.

# crud company by us

class CompanyViewSet(viewsets.ModelViewSet):
    
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class CompanyActivation(UpdateAPIView):
    serializer_class = CompanySerializer

    def get_object(self , **kwargs):
        return Company.objects.get(**kwargs)

    def update(self, request, *args, **kwargs):
        obj = self.get_object(**kwargs)
        obj.is_active = True
        serialized_data = self.serializer_class(obj)
        pass
