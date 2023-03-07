from django.urls import path
from . import views
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path("usuarios/", views.UserView.as_view()),
    path("usuarios/<int:pk>/", views.UserDetailView.as_view()),
    path("usuarios/login/", jwt_views.TokenObtainPairView.as_view()),
]