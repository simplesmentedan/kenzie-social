from rest_framework import permissions
from .models import Publicacao
from rest_framework.views import View, Request
from rest_framework.permissions import SAFE_METHODS

class IsPostOwnerOrReadyOnly(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View, obj: Publicacao) -> bool:
        return bool(
           request.method in SAFE_METHODS or
           request.user.is_authenticated and request.user == obj.owner   
        )

       