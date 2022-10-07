from django.urls import path
from .routers import router
urlpatterns = [] + router.urls