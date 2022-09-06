from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
   path('genre/save/' , GenreRegister.as_view()),
   path('genre/filter/' , GenreFilter.as_view()),
   path('genre/delete/' , DeleteGenre.as_view()),
   path('class/save/' , ClassRegister.as_view()),
   
   path('class/all/',GetBookClasses.as_view()),
   path('class/delete/' , ClassDelete.as_view()),
   path('object/save/' , ObjectRegister.as_view()),
   path('object/<str:name>', GetBookObjectsWithSlug.as_view()),
   path('object/delete/', ObjectDelete.as_view())
]
