from django.urls import path
from .views import RegisterAPI,LoginAPI,LogoutAPI



urlpatterns = [
    
    path('registration/',RegisterAPI.as_view()),
    path('log/',LoginAPI.as_view()),
    path('out/',LogoutAPI.as_view())
]
