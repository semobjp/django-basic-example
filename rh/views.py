from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.urls import reverse
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
            messages.success(request, "User created successfully")
            return redirect(reverse("rh:user_perfil_create"))

    return render(request, 'user_perfil_create.html', locals())
