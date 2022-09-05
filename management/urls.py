from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
   path('new-admin/' , SignUpAdmin.as_view()),
   path('update-admin/' ,UpdateAdmin.as_view()),
   path('delete-admin/',DeleteAdmin.as_view()),
   path('deactive/' , DeActivateAdmin.as_view()),
   path('active/' , ActivateAdmin.as_view()),
   path('over-all-admin-views/' , OverallViewOnAdmins.as_view()),
   path('leave-admin/' , LeaveAdmin.as_view()),
   path('query-admin/',FilterAdmins.as_view()),
   path('over-all-customer-views/' , OverallViewOnCustomers.as_view()),
   path('query-customer/' , CustomerFilter.as_view()),
   path('my-profile/', GetProfileAPIView.as_view())
]
