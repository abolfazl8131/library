from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
   path('save-genre/' , GenreRegister.as_view()),
   path('filter-genre/' , GenreFilter.as_view()),
   path('delete-genre/' , DeleteGenre.as_view()),
   path('save-class/' , ClassRegister.as_view()),
   
   path('class-all/',GetBookClasses.as_view()),
   path('delete-class/' , ClassDelete.as_view()),
   path('save-object/' , ObjectRegister.as_view()),
   path('object/<str:name>', GetBookObjectsWithSlug.as_view()),
   path('object-delete/', ObjectDelete.as_view())
]
