from django.urls import path
from . import views

urlpatterns = [
    path("seguidores/<int:pk>", views.SeguidoresView.as_view()),
]