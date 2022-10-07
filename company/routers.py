from .views import CompanyViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'', CompanyViewSet, basename='company')
