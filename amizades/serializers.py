from rest_framework import serializers


class AmizadesSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    id_pendent = serializers.IntegerField(source="user.id")
    first_name = serializers.CharField(source="user.first_name")
    last_name = serializers.CharField(source="user.last_name")
    username = serializers.CharField(source="user.username")
