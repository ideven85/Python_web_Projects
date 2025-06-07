from django.test import TestCase
from django.urls import reverse

from ourwedding.forms import GuestEditForm, GuestProfileForm, GuestCreateForm
from ourwedding.models import Profile, Group
from ourwedding.tokens import login_token_generator


class TestGuestPages(TestCase):
    def setUp(self):
        self.guest = Profile.objects.create(
            first_name="Aquiles", last_name="Carattino", email="lala@lolo.com"
        )
        self.guest.save()
        token = login_token_generator.make_token(self.guest)
        response = self.client.get(reverse("guest-login"), data={"access_code": token})
        self.assertEqual(self.client.session["guest"], self.guest.id)
        self.guest_other = Profile.objects.create(
            first_name="Aqui", last_name="Cara", email="aqui@cara.com"
        )

    def test_access_all_views(self):
        """Test that all the views return 200"""
        views = [
            "save-the-date",
            "home",
            "code-sent",
            "guest-login",
            "home-forbidden",
            "profile",
            "RSVP",
            "guest-add",
            "list-messages",
            "create-message",
            "contact",
            "register",
            "event",
            "help",
        ]

        for view in views:
            response = self.client.get(reverse(view))
            self.assertEqual(response.status_code, 200, view)

    def test_profile_edit(self):
        data = {
            "first_name": "AquilesF",
            "last_name": "CarattinoF",
            "email": "email@email.comF",
            "phone": "12345",
            "language": "en",
            "is_attending": True,
        }

        form = GuestProfileForm(data)
        self.assertTrue(form.is_valid())
        response = self.client.post(reverse("profile"), data=data)
        self.assertRedirects(response, reverse("profile"))
        self.assertTrue(Profile.objects.get(email="email@email.comF"))

    def test_guest_add(self):
        """Test the ability to add another guest."""
        data = {
            "first_name": "New First Name",
            "last_name": "New Last Name",
            "email": "new_email@mail.com",
            "is_attending": False,
            "is_child": False,
        }
        form = GuestCreateForm(data)
        self.assertTrue(form.is_valid())
        response = self.client.post(reverse("guest-add"), data=data)
        self.assertRedirects(response, reverse("RSVP"))
        self.assertTrue(
            Group.objects.filter(name=self.guest.first_name).exists(),
            "New Group not created",
        )
        self.assertTrue(
            Profile.objects.filter(email="new_email@mail.com").exists(),
            "New guest not created",
        )

    def test_guest_not_add(self):
        pass
