from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import IsAuthenticatedOrReadOnly
from .models import Curtida
from .serializers import CurtidaSerializer
from django.shortcuts import get_object_or_404
from publicacoes.models import Publicacao
from rest_framework.views import Response, Request, status


class CurtidaView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Curtida.objects.all()
    serializer_class = CurtidaSerializer

    def get(self, request: Request, pk: int):
        post = get_object_or_404(Publicacao, pk=pk)
        likes = Curtida.objects.filter(post=post)
        serializer = CurtidaSerializer(likes, many=True)

        return Response(serializer.data, status.HTTP_200_OK)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CurtidaDetailView(RetrieveDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Curtida.objects.all()
    serializer_class = CurtidaSerializer
