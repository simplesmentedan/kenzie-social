from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView, Response, Request
from django.shortcuts import get_object_or_404
from usuarios.models import Usuario
from .models import Seguidores


import json
# Create your views here.


class SeguidoresView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def patch(self, request: Request, pk:int):
        if request.user.id == pk:  
            return Response({"message": "can't follow yourself"}, 403)

        seguindo = get_object_or_404(Usuario, id=pk)
        Seguidores.objects.create(seguindo=seguindo, seguidor=request.user)

        return Response({"message": "Successfully followed user"}, 200)

