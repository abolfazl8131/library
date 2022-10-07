from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
   path('admin/save/' , SignUpAdmin.as_view()),
   path('admin/update/' ,UpdateAdmin.as_view()),
   path('admin/delete/',DeleteAdmin.as_view()),
   path('admin/deactivate/' , DeActivateAdmin.as_view()),
   path('admin/activate/' , ActivateAdmin.as_view()),
   path('admin/all/' , OverallViewOnAdmins.as_view()),
   path('admin/leave/' , LeaveAdmin.as_view()),
   path('admin/query/',FilterAdmins.as_view()),
   path('over-all-customer-views/' , OverallViewOnCustomers.as_view()),
   path('query-customer/' , CustomerFilter.as_view()),
   path('profile/', GetProfileAPIView.as_view()),
   path('admin/master/register/', RegisterMasterOfCompany.as_view())
]








