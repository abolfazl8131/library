from django.urls import path
from .views import SignUp, GetProfile, UpdateProfile


urlpatterns = [
    path('sign-up/' , SignUp.as_view()),
    path('profile/' , GetProfile.as_view() , name = 'profile view'),
    path('update/' , UpdateProfile.as_view())
]