from django.urls import path
from .views import *
from rest_framework_simplejwt import views as jwt_views


urlpatterns = [
  
    path('customer-enter-ID/' , EnterID.as_view()),
    path('customer-sign-code/' , EnterAuthCode.as_view()),
    path('admin/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('admin/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
   
]