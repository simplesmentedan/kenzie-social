from rest_framework import serializers
from .models import Publicacao
from usuarios.serializers import UserSerializer


class PublicacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publicacao
        fields = [
            "id",
            "title",
            "content",
            "created_date",
            "post_type",
            "owner_id"
        ]