from django.urls import path
from .views import RegisterUserAPIView, GetUserInfoAPIView

urlpatterns = [
    path("register/", RegisterUserAPIView.as_view()),
    path('api/user/<int:user_id>/', GetUserInfoAPIView.as_view())
]