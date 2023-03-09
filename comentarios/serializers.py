from rest_framework import serializers
from .models import Comentario

class ComentarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comentario
        fields = ["id", "owner_id", "post_id",  "created_date", "content"]
            
            
            
            
        