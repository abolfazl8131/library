from audioop import add
from django.urls import path
from .views import AddToBasket , DeleteBasket , GetBasket , Rent
urlpatterns = [
    path('basket/add/' , AddToBasket.as_view()),
    path('basket/delete/' , DeleteBasket.as_view()),
    path('basket/get/' , GetBasket.as_view()),
    path('loan/' ,Rent.as_view() )
   
]