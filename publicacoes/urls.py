from django.urls import path
from . import views

urlpatterns = [
    path("postagens/", views.PublicacaoView.as_view()),
    path("postagens/<int:pk>/", views.PubicacaoDetailView.as_view())
]