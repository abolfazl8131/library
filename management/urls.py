from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
   path('new-admin/' , SignUpAdmin.as_view()),
   path('update-admin/' ,UpdateAdmin.as_view())
]
