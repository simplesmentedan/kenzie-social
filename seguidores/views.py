from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView, Response, Request
from django.shortcuts import get_object_or_404
from usuarios.models import Usuario
from .models import Seguidores
from .serializers import SeguidoresSerializer
from django.forms.models import model_to_dict


import json
# Create your views here.


class SeguidoresView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request: Request, pk:int):
        if request.user.id == pk:  
            return Response({"message": "can't follow yourself"}, 403)

        seguindo = get_object_or_404(Usuario, id=pk)
        Seguidores.objects.create(seguindo=seguindo, seguidor=request.user)
        return Response({"message": "Successfully followed user"}, 200)
    
    def get(self, request: Request):
        seguidores = Seguidores.objects.filter(seguindo=request.user)
        serializer = SeguidoresSerializer(seguidores, many=True)

        return Response(serializer.data)

