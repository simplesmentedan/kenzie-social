from rest_framework import generics

from comentarios.permissions import IsComentarioOwnerOrReadyOnly
from .models import Comentario
from .serializers import ComentarioSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class ComentarioView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user,post_id=self.kwargs["pk"])


class ComentarioDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsComentarioOwnerOrReadyOnly]

    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer   

  

