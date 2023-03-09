from django.db import models
from publicacoes.models import Publicacao

class Comentario(models.Model):
    owner = models.ForeignKey( "usuarios.Usuario",on_delete=models.CASCADE,related_name="comentario")
    post  = models.ForeignKey(Publicacao, on_delete=models.CASCADE,related_name="comentario")
    created_date = models.DateField(auto_now_add=True)
    content = models.TextField()

       
        
        
    

