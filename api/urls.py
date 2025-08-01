from django.urls import path
from .views import (
    StudentListCreate,
    OfficeListCreate,
    StudentDetailAPIView
  
    )




urlpatterns = [
    
    path('student/', StudentListCreate.as_view(), name='student'),
    path('stud/<int:pk>',StudentDetailAPIView.as_view(),name='stud-detail'),
    path('office/',OfficeListCreate.as_view(),name='office')
]
