from datetime import date

from django.test import TestCase
from django.urls import reverse

from ourwedding.forms import RegisterForm
from ourwedding.models import Profile
from ourwedding.tokens import login_token_generator


class SaveTheDate(TestCase):
    def setUp(self):
        self.email = "lala@lolo.com"
        self.guest = Profile.objects.create(
            first_name="Aquiles", last_name="Carattino", email=self.email
        )
        self.guest.save()
        self.token = login_token_generator.make_token(self.guest)

    def test_login_page(self):
        response = self.client.get(reverse("guest-login"))
        self.assertEqual(response.status_code, 200)

    def test_token_home_redirect(self):
        token = login_token_generator.make_token(self.guest)
        response = self.client.get(reverse("guest-login"), data={"access_code": token})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse("home"))
        self.assertEqual(self.client.session["guest"], self.guest.id)

    def test_token_next_redirect(self):
        token = login_token_generator.make_token(self.guest)
        response = self.client.get(
            reverse("guest-login"), data={"access_code": token, "next": "save-the-date"}
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse("save-the-date"))

    def test_expired_token(self):
        ts = login_token_generator._num_days(date(2019, 1, 1))
        token = login_token_generator._make_token_with_timestamp(self.guest, ts)
        response = self.client.get(reverse("guest-login"), data={"access_code": token})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Expired")

    def test_wrong_token(self):
        token = "12345"
        self.assertFalse(login_token_generator.check_token(self.guest, None))
        self.assertFalse(login_token_generator.check_token(self.guest, token))
        token = "abc-123-123"
        self.assertFalse(login_token_generator.check_token(self.guest, token))
        valid_token = login_token_generator.make_token(self.guest)
        self.assertTrue(login_token_generator.check_token(self.guest, valid_token))
        ts = login_token_generator._num_days(date(2019, 1, 1))
        expired_token = login_token_generator._make_token_with_timestamp(self.guest, ts)
        self.assertFalse(login_token_generator.check_token(self.guest, expired_token))

    def test_send_token(self):
        response = self.client.post(reverse("guest-login"), data={"email": self.email})
        self.assertContains(response, "sent")

    def test_send_token_wrong_email(self):
        response = self.client.post(
            reverse("guest-login"), data={"email": "wrong@email.com"}
        )
        self.assertContains(response, "registering")

    def test_non_valid_email(self):
        response = self.client.post(reverse("guest-login"), data={"email": "wrong"})
        self.assertContains(response, "There were errors processing your form")

    def test_home(self):
        token = login_token_generator.make_token(self.guest)
        self.client.get(reverse("guest-login"), data={"access_code": token})
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "ourwedding/index.html")

    def test_valid_register(self):
        data = {
            "first_name": "First Name",
            "last_name": "Last Name",
            "email": "email@email.com",
            "language": "es",
        }

        form = RegisterForm(data=data)
        self.assertTrue(form.is_valid())
        response = self.client.post(reverse("register"), data=data)
        self.assertContains(response, "Thank you")

    def test_existing_register(self):
        data = {
            "first_name": "First Name",
            "last_name": "Last Name",
            "email": self.email,
            "language": "es",
        }
        response = self.client.post(reverse("register"), data=data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse("guest-login"))

    def test_wrong_data(self):
        wrong_data = [
            # Missing First name
            {"last_name": "Last Name", "email": "new@email.com", "language": "es"},
            # Missing Last Name
            {"first_name": "First Name", "email": "new@email.com", "language": "es"},
        ]
        for data in wrong_data:
            response = self.client.post(reverse("register"), data=data)
            self.assertEqual(response.status_code, 200)
            self.assertContains(response, "This field is required")

        data = {
            "first_name": "First Name",
            "last_name": "Last Name",
            "email": "new@email",
            "language": "es",
        }
        form = RegisterForm(data)
        self.assertFalse(form.is_valid())
        response = self.client.post(reverse("register"), data=data)
        self.assertNotContains(response, "This field is required")
        self.assertContains(response, "invalid")

    def test_register_logged_in(self):
        self.client.get(reverse("guest-login"), data={"access_code": self.token})
        self.assertEqual(self.client.session["guest"], self.guest.id)
        response = self.client.get(reverse("register"))
        self.assertContains(response, "You are already logged in")

    def test_login_redirect(self):
        response = self.client.get(reverse("list-messages"))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse("guest-login") + "?next=/messages")
