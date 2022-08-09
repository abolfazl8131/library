from django.urls import path
from .views import *


urlpatterns = [
  
    path('customer-enter-ID/' , EnterID.as_view()),
    path('customer-sign-code/' , EnterAuthCode.as_view()),
   
]