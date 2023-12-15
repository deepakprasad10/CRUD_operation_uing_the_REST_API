from django.urls import path
from .views import *
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [
   path('register/',view_register),
   path('secure/',view_secure),
   path('login/',obtain_auth_token),    
   path('employee/', EmployeeDetail.as_view(), name='employeedetail'),
   path('employee/<int:id>/', EmployeeInfo.as_view(), name='employeeinfo'),
    
]
