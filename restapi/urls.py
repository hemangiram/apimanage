from django.urls import path
from .views import (
    NurseListCreate, NurseDetail,
    PatientListCreate, PatientDetail,
    DoctorListCreate, DoctorDetail,ImageUploadAPIView,FileUploadAPIView
)

urlpatterns = [
    path('nurse/', NurseListCreate.as_view()),
    path('nurse/<int:pk>/', NurseDetail.as_view()),

    path('patient/', PatientListCreate.as_view()),
    path('patient/<int:pk>/', PatientDetail.as_view()),

    path('doctor/', DoctorListCreate.as_view()),
    path('doctor/<int:pk>/', DoctorDetail.as_view()),

    path('image/',ImageUploadAPIView.as_view(),name='upload-image'),
    path('upload/', FileUploadAPIView.as_view(), name='upload'),
    
    ]
