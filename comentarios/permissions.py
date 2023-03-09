from rest_framework import permissions
from .models import Comentario
from rest_framework.views import View, Request
from rest_framework.permissions import SAFE_METHODS

class IsComentarioOwnerOrReadyOnly(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View, obj: Comentario) -> bool:
        return bool(
           request.method in SAFE_METHODS or
           request.user.is_authenticated and request.user == obj.owner   
        )