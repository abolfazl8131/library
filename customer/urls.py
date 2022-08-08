from django.urls import path
from .views import *


urlpatterns = [
    path('sign-up/' , SignUp.as_view()),
    path('sign-in/' , EnterID.as_view()),
    path('sign-code/' , EnterAuthCode.as_view()),
    path('profile/' , GetProfile.as_view() , name = 'profile view'),
    path('update/' , UpdateProfile.as_view())
]