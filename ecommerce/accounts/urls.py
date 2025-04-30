from django.urls import path
from .views import RegisterAPIView, CustomTokenObtainPairView, UserProfileView, register_page, login_page


urlpatterns = [
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('login/', CustomTokenObtainPairView.as_view(), name='login'),
    path('profile/', UserProfileView.as_view(), name='user_profile'),
    path('register-page/', register_page, name='register-page'),
    path('login-page/', login_page, name='login-page'),
]
