from rest_framework.views import APIView, Request, Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from usuarios.models import Usuario
from .models import Amizades
from .serializers import AmizadesSerializer
from rest_framework import generics

# Create your views here.
class AmizadesView(generics.GenericAPIView):
    authentication_classes= [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Amizades.objects.all()
    serializer_class = AmizadesSerializer
    
    
    def post(self, request: Request, pk:int):
        if request.user.id == pk:
            return Response({"message": "Not permission"})
        
        friend = get_object_or_404(Usuario, id=pk)
        Amizades.objects.create(pendent_friend=friend, friend=None, user=request.user)
        return Response({"message": "Friendship invitation sent successfully"}, 201)

    def patch(self, request: Request, pk:int):
        solicitacao: Amizades = get_object_or_404(Amizades, id=pk)
        aceitante = request.user
        solicitacao.friend = aceitante
        solicitacao.pendent_friend = None
        solicitacao.save()

        return Response({"message": "friend request accepted"})
    
    def get(self, request: Request):
        solicitacoes = Amizades.objects.filter(pendent_friend=request.user)
        serializer = AmizadesSerializer(solicitacoes, many=True)

        return Response(serializer.data)