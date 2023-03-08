from rest_framework import serializers
from .models import Usuario
from rest_framework.validators import UniqueValidator


class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data: dict) -> Usuario:
        return Usuario.objects.create_superuser(**validated_data)

    def update(self, instance: Usuario, validated_data: dict) -> Usuario:
        for key, value in validated_data.items():
            if key == "password":
                instance.set_password(validated_data["password"])
            else:
                setattr(instance, key, value)

        instance.save()

        return instance
    
    class Meta:
        model = Usuario
        fields = ["id", "username", "email", "password", "first_name", "last_name"]
        extra_kwargs = {"password": {"write_only": True}, 'email': {
                    'validators': [
                        UniqueValidator(
                            queryset=Usuario.objects.all()
                        ),
                    ],
                    "required": True
                }}
