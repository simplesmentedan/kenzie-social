from django.urls import path
from . import views
from curtidas import views as curtida_views

urlpatterns = [
    path("postagens/", views.PublicacaoView.as_view()),
    path("postagens/<int:pk>/", views.PubicacaoDetailView.as_view()),
    path("postagens/<int:pk>/curtidas/", curtida_views.CurtidaView.as_view()),
]
