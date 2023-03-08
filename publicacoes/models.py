from django.db import models

class PublicacaoChoices(models.TextChoices):
    PUBLIC = "public"
    PRIVATE = "private"

class Publicacao(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_date = models.DateField(auto_now_add=True)
    post_type = models.CharField(
        max_length=50,
        choices=PublicacaoChoices.choices,
        default=PublicacaoChoices.PUBLIC
    )

    owner = models.ForeignKey(
        "usuarios.Usuario",
        on_delete=models.CASCADE,
        related_name="posts"
    )