from django.db import models
from django.contrib.auth.models import User


class Perfil(models.Model):
    """
    Modelo responsável por armazenar informações referentes aos perfis de cada usuário.

    Por meio deste modelo nós criamos um vínculo entre o modelo User e informações que venham
    a ser pertinentes para a sua extenção.
    """
    user = models.OneToOneField(User)
    cidade = models.CharField(max_length=100)

    def __str__(self):
        return "Perfil do usuário: {}".format(self.user.pk)
