from django.db import models
import datetime


class Curtida(models.Model):
    liked_at = models.DateField(
        default=datetime.date.today,
        null=True
    )
    owner = models.ForeignKey(
        "usuarios.Usuario",
        on_delete=models.CASCADE,
        related_name="likes"
    )
    post = models.ForeignKey(
        "publicacoes.Publicacao",
        on_delete=models.CASCADE,
        related_name="likes"
    )
