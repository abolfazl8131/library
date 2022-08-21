from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
   path('save-genre/' , GenreRegister.as_view()),
   path('filter-genre/' , GenreFilter.as_view())
]
