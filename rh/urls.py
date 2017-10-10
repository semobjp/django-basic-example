from django.conf.urls import url
from rh import views

urlpatterns = [
    url(r'^$', views.user_perfil_create,
        name="user_perfil_create"),
]
