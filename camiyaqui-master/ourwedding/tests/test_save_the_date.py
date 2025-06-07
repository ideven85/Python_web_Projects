from django.test import TestCase
from django.urls import reverse

from ourwedding.models import Profile


class SaveTheDate(TestCase):
    def setUp(self):
        self.guest = Profile.objects.create(
            first_name="Aquiles", last_name="Carattino", email="lala@lolo.com"
        )
        self.guest.save()

    def test_secret_code_redirect(self):
        response = self.client.get(
            reverse("secret-code-validation", args=[self.guest.secret_code])
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse("save-the-date"))

    def test_invalid_secret_code(self):
        response = self.client.get(reverse("secret-code-validation", args=["1234abcd"]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse("guest-login"))

    def test_save_the_date_view(self):
        response = self.client.get(
            reverse("secret-code-validation", args=[self.guest.secret_code])
        )
        response = self.client.get(response.url)
        self.assertTemplateUsed(response, "savethedate/index_es.html")
        self.guest.language = "en"
        self.guest.save()
        response = self.client.get(
            reverse("secret-code-validation", args=[self.guest.secret_code])
        )
        response = self.client.get(response.url)
        self.assertTemplateUsed(response, "savethedate/index_en.html")
        self.guest.language = "es"
        self.guest.save()
