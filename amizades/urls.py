from django.urls import path
from . import views
from .views import AmizadesView

urlpatterns = [
    path("amizades/", views.AmizadesView.as_view()),
    path("amizades/<int:pk>", views.AmizadesView.as_view()),
]