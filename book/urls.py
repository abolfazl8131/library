
from django.urls import path
from .views import (GenreRegister, 
               GenreFilter, 
               DeleteGenre,
               ClassDelete,
               ObjectDelete,
               ClassRegister,
               GetBookClasses,
               ObjectRegister,
               GetBookObjectsWithSlug,
               UploadImage)

urlpatterns = [
   path('genre/save/' , GenreRegister.as_view()),
   path('genre/filter/' , GenreFilter.as_view()),
   path('genre/delete/' , DeleteGenre.as_view()),
   path('class/save/' , ClassRegister.as_view()),
   
   path('class/all/',GetBookClasses.as_view()),
   path('class/delete/' , ClassDelete.as_view()),
   path('object/save/' , ObjectRegister.as_view()),
   path('object/<str:name>', GetBookObjectsWithSlug.as_view()),
   path('object/delete/', ObjectDelete.as_view()),

   path('image/load/' , UploadImage.as_view())
]