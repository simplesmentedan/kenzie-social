from rest_framework import generics
from .models import Publicacao
from .serializers import PublicacaoSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import IsPostOwnerOrReadyOnly
from rest_framework.views import Request, Response, status
from django.shortcuts import get_object_or_404

class PublicacaoView(generics.CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Publicacao.objects.all()
    serializer_class = PublicacaoSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class PubicacaoDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsPostOwnerOrReadyOnly]
    queryset = Publicacao.objects.all()
    serializer_class = PublicacaoSerializer

    def get(self, request: Request, pk: int):
        current_post = get_object_or_404(Publicacao, id=pk)
        if current_post.post_type == "public":
            serializer = PublicacaoSerializer(current_post)
            return Response(serializer.data, status.HTTP_200_OK)
        elif bool(current_post.post_type == "private" and request.user.is_authenticated == True):
            serializer = PublicacaoSerializer(current_post)
            return Response(serializer.data, status.HTTP_200_OK)
        else:
            return Response(
                {"message": "This publication require authentication and user follow or user added in your friends!"},
                status.HTTP_403_FORBIDDEN
            )
