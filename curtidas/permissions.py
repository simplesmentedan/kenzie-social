from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework.views import Request, View
from .models import Curtida


class IsAuthenticatedOrReadOnly(BasePermission):
    def has_object_permission(self, request: Request, view: View, obj: Curtida) -> bool:
        return bool(
            request.method in SAFE_METHODS or
            request.user.is_authenticated and request.user == obj.owner
        )
