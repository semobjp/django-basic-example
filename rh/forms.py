from django import forms
from rh.models import Perfil


class UserPerfilForm(forms.ModelForm):
    """
    Formulário responsável por capturar informações de perfil para um usuário.
    Por meio deste formulário nós mapeamos o modelo Perfil e renderizamos em forma
    de elementos HTML, sendo possível capturar dados para cadastro e atualização.

    prefix: str - Utilizado para tornar o formulário distinguível entre formulários na mesma requisição
    """
    prefix = "perfil"

    class Meta:
        model = Perfil
        exclude = ['user']