from django.db import models

# Create your models here.
from django.conf import settings


class PerfilUsuario(models.Model):

    user = models.OneToOneField(settings.AUTH_USER_MODEL)

    def __str__(self):
        return self.user.username
   