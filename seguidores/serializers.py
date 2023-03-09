from rest_framework import serializers


class SeguidoresSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    id_follower = serializers.IntegerField(source="seguidor.id") 
    first_name = serializers.CharField(source="seguidor.first_name")
    last_name = serializers.CharField(source="seguidor.last_name")
    username = serializers.CharField(source="seguidor.username")
  
