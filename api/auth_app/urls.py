from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

from .views import RegisterApi, UserApi

urlpatterns = [
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/register/', RegisterApi.as_view(), name='register_user'),
    path('api/user/', UserApi.as_view(), name='current_user')
]