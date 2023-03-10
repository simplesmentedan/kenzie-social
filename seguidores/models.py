from django.db import models

# Create your models here.

class Seguidores(models.Model):
      seguindo = models.ForeignKey("usuarios.Usuario", on_delete=models.CASCADE, related_name="following")
      seguidor = models.ForeignKey("usuarios.Usuario", on_delete=models.CASCADE, related_name="followers")
      
