
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
               UploadImage,ObjectFind , RecommendorTest,FilterBookClassesWithCompany)

urlpatterns = [
   path('genre/save/' , GenreRegister.as_view()),
   path('genre/filter/' , GenreFilter.as_view()),
   path('genre/delete/' , DeleteGenre.as_view()),
   path('class/save/' , ClassRegister.as_view()),
   path('class/filter/',FilterBookClassesWithCompany.as_view()),
   path('class/all/',GetBookClasses.as_view()),
   path('class/delete/' , ClassDelete.as_view()),
   path('object/save/' , ObjectRegister.as_view()),
   path('object/<str:name>', GetBookObjectsWithSlug.as_view()),
   path('object/delete/', ObjectDelete.as_view()),
   #path('object/find/', ObjectFind.as_view()),
   path('image/load/' , UploadImage.as_view()),
   path('test/', RecommendorTest.as_view() ),
   
]