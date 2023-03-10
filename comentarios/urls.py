from django.urls import path
from . import views

urlpatterns = [
    path("<int:pk>/comentarios/", views.ComentarioView.as_view()),
    path("comentarios/<int:pk>/", views.ComentarioDetailView.as_view())
]