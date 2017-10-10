from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from rh.forms import UserPerfilForm



def user_perfil_create(request):
    """
    View responsável por criar um usuário e seu perfil associado
    """
    perfil_form = UserPerfilForm()
    user_form = UserCreationForm(prefix="user")

    if request.method == "POST":
        user_form = UserCreationForm(request.POST, prefix="user")
        perfil_form = UserPerfilForm(request.POST)

        if user_form.is_valid() and perfil_form.is_valid():
            user = user_form.save()
            perfil = perfil_form.save(commit=False)
            perfil.user = user
            perfil.save()



    return render(request, 'user_perfil_create.html', locals())
