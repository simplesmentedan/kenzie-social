from rest_framework import permissions
from .models import Usuario
from rest_framework.views import View,Request
from rest_framework.permissions import SAFE_METHODS

class IsAccountOwner(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View, obj: Usuario) -> bool:
        return request.method in SAFE_METHODS or request.user.is_authenticated and obj == request.user

        