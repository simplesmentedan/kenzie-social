from django.urls import path
from . import views

urlpatterns = [
    path("curtidas/", views.CurtidaView.as_view()),
    path("curtidas/<int:pk>/", views.CurtidaDetailView.as_view()),
]
