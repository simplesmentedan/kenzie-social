from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView, Response, Request
from rest_framework import generics
from django.shortcuts import get_object_or_404
from usuarios.models import Usuario
from .models import Seguidores
from .serializers import SeguidoresSerializer


# Create your views here.
class SeguidoresView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Seguidores.objects.all()
    serializer_class = SeguidoresSerializer
   

    def post(self, request: Request, pk:int):
        if request.user.id == pk:  
            return Response({"message": "can't follow yourself"}, 403)

        seguindo = get_object_or_404(Usuario, id=pk)
        Seguidores.objects.create(seguindo=seguindo, seguidor=request.user)
        return Response({"message": "Successfully followed user"}, 201)
    
    def get(self, request: Request):
        seguidores = Seguidores.objects.filter(seguindo=request.user)
        serializer = SeguidoresSerializer(seguidores, many=True)

        return Response(serializer.data)

