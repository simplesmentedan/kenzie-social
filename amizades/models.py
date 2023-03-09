from django.db import models

# Create your models here.
class Amizades(models.Model):
    friend = models.ForeignKey("usuarios.Usuario", on_delete=models.CASCADE, related_name="friends", null=True)
    pendent_friend = models.ForeignKey("usuarios.Usuario", on_delete=models.CASCADE, related_name="pendents_friends", null=True)
    user = models.ForeignKey("usuarios.Usuario", on_delete=models.CASCADE, related_name="user_firends")
    