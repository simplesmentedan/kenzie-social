from rest_framework import serializers
from .models import Curtida


class CurtidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curtida
        fields = [
            "id",
            "owner",
            "post",
            "liked_at",
        ]
        extra_kwargs = {
            "owner": {"read_only": True},
            "liked_at": {"read_only": True}
        }

    def create(self, validated_data):
        post_id = validated_data['post']
        if Curtida.objects.filter(post=post_id).exists():
            raise serializers.ValidationError(
                "User already liked this post."
            )

        return Curtida.objects.create(**validated_data)
