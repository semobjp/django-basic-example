from django.test import TestCase, Client
from django.urls import reverse
from model_mommy import mommy
from rh.models import Perfil


class RHTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.form_data = {
            "user-username": "tester",
            "user-password1": "testerrandompass987",
            "user-password2": "testerrandompass987",
            "perfil-cidade": "some city"
        }

    def test_perfil_model(self):
        perfil = mommy.make(Perfil)
        self.assertEqual("Perfil do usuário: {}".format(perfil.user.pk), str(perfil))

    def test_access_view(self):
        response = self.client.get(reverse("rh:user_perfil_create"))
        self.assertEqual(200, response.status_code)

    def test_create_user_with_profile(self):
        response = self.client.post(reverse("rh:user_perfil_create"),
                                    self.form_data, follow=True)
        self.assertIn("User created successfully", response.content.decode())
        self.assertRedirects(response, reverse("rh:user_perfil_create"))


