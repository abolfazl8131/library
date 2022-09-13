from audioop import add
from django.urls import path
from .views import AddToBasket , DeleteBasket , GetBasket , Rent , AdminRentListAPIView , AdminGetRentObjectAPIView
urlpatterns = [
    path('basket/add/' , AddToBasket.as_view()),
    path('basket/delete/' , DeleteBasket.as_view()),
    path('basket/get/' , GetBasket.as_view()),
    path('rent/save/' ,Rent.as_view() ),
    path('rent/list/admin' , AdminRentListAPIView.as_view()),
    path('rent/get/admin' , AdminGetRentObjectAPIView.as_view() )
   
]