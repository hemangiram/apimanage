from .models import Fruit
from django.urls import path
from .views import (
         FruitListCreate,
         FruitDetailAPIView,
         ActiveFruitListView
)
from rest_framework_simplejwt import views as jwt_views
urlpatterns = [
    path('fruit/', FruitListCreate.as_view(),name='fruit'),
    path('fruit/<int:pk>/', FruitDetailAPIView.as_view(),name='fruit-details'),
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),

    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('fruit/active/', ActiveFruitListView.as_view(), name='active-fruit-list'),
]

