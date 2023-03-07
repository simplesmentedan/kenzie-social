from rest_framework import generics
from .models import Usuario
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import UserSerializer
from .permissions import IsAccountOwner


class UserView(generics.CreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UserSerializer


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwner]

    queryset = Usuario.objects.all()
    serializer_class = UserSerializer


