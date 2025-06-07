import os
import uuid

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.timezone import now
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from django.core.mail import EmailMultiAlternatives, EmailMessage
from django.db import models
from django.template import Template, Context
from rest_framework.authtoken.models import Token

from ourwedding.tokens import login_token_generator


class Group(models.Model):
    """A group of guests coming together. It can be a Family, a couple, etc."""

    name = models.CharField(max_length=150)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Group {}".format(self.id)


class Profile(models.Model):
    """A single guest"""

    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    nickname = models.CharField(_("nickname"), max_length=25, null=True, blank=True)
    language = models.CharField(
        _("language"), max_length=2, choices=settings.LANGUAGES, default="es"
    )
    phone = models.CharField(_("phone"), max_length=13, null=True, blank=True)
    invited_by = models.ForeignKey(
        User,
        related_name="invited_by",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    group = models.ForeignKey(
        Group, related_name="members", on_delete=models.SET_NULL, null=True, blank=True
    )

    is_attending = models.NullBooleanField(
        _("is attending"), default=None, help_text=_("Are you attending?")
    )
    is_child = models.BooleanField(
        _("is child"), default=False, help_text=_("Under 12")
    )

    receive_updates = models.BooleanField(
        _("receive updates"),
        default=True,
        help_text=_(
            "Even if you are not attending, we can keep you in the loop with photos, etc."
        ),
    )

    last_login = models.DateTimeField(
        auto_now_add=False, default=None, null=True, blank=True
    )

    has_car = models.BooleanField(
        _("Car"), default=False, help_text=_("Do you have a car?")
    )
    needs_van = models.BooleanField(
        _("Van"), default=False, help_text=_("Do you need transport?")
    )
    dietary_restrictions = models.TextField(blank=True, null=True, default=None)
    comes_from = models.TextField(_("Coming from"), blank=True, null=True, default=None)
    pre_wedding = models.BooleanField(
        _("pre wedding"),
        default=False,
        help_text=_("Are you attending the pre-wedding?"),
    )
    post_wedding = models.BooleanField(
        _("post wedding"),
        default=False,
        help_text=_("Are you attending the post-wedding?"),
    )

    @property
    def access_code(self):
        return login_token_generator.make_token(self.user)

    @property
    def first_name(self):
        return self.user.first_name

    @property
    def last_name(self):
        return self.user.last_name

    @property
    def email(self):
        return self.user.email

    def send_code(self):
        """Sends the access code by e-mail."""
        token = login_token_generator.make_token(self.user)

        # Default to english
        template_email = os.path.join(
            settings.BASE_DIR, "templates", "emails", "access_token_en.txt"
        )
        if self.language == "es":
            template_email = os.path.join(
                settings.BASE_DIR, "templates", "emails", "access_token_es.txt"
            )

        with open(template_email, "r", encoding="utf-8") as f:
            file = f.read()

        tmpl_txt = Template(file)
        context = Context(
            {"guest": self, "token": token, "domain": settings.WEBSITE_URL}
        )
        msg_txt = tmpl_txt.render(context=context)
        msg = EmailMultiAlternatives(
            "Access Code",
            msg_txt,
            settings.EMAIL_FROM,
            [self.user.email],
            reply_to=[settings.EMAIL_FROM],
        )
        msg.send()

    def __str__(self):
        if self.nickname:
            return self.nickname
        if self.user.first_name and self.user.last_name:
            return self.user.first_name + " " + self.user.last_name
        return str(self.id)

    class Meta:
        ordering = ["-is_attending"]


class Guest(models.Model):
    """Model for holding information on guests who are either invited by someone else or are waiting for
    approval. Once a guest is approved, it either changes a flag or is moved to become a User.
    """

    first_name = models.CharField(max_length=255, blank=False, null=False)
    last_name = models.CharField(max_length=255, blank=False, null=False)
    email = models.EmailField(blank=True, null=True)

    dietary_restrictions = models.TextField(blank=True)
    is_attending = models.NullBooleanField(
        _("is attending"), default=None, help_text=_("Are you attending?")
    )
    is_child = models.BooleanField(
        _("is child"), default=False, help_text=_("Under 12")
    )
    phone = models.CharField(_("phone"), max_length=13, null=True, blank=True)
    has_car = models.BooleanField(default=False)
    invited_by = models.ForeignKey(
        User, related_name="invites", on_delete=models.SET_NULL, null=True, blank=True
    )
    comes_from = models.TextField(blank=True, null=True, default=None)
    needs_van = models.BooleanField(
        _("Van"), default=False, help_text=_("Do you need transport?")
    )
    pre_wedding = models.BooleanField(
        _("pre wedding"),
        default=False,
        help_text=_("Are you attending the pre-wedding?"),
    )
    post_wedding = models.BooleanField(
        _("post wedding"),
        default=False,
        help_text=_("Are you attending the post-wedding?"),
    )

    def __str__(self):
        return self.first_name + " " + self.last_name


class MessageFromGuest(models.Model):
    """For people using the 'contact' form."""

    timestamp = models.DateTimeField(auto_now_add=True)
    message = models.TextField()
    guest = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    opened = models.BooleanField(default=False)  # Viewed on the website
    opened_on = models.DateTimeField(auto_now_add=False, default=None, null=True)
    notified = models.BooleanField(default=False)  # Notified by e-mail
    notified_on = models.DateTimeField(auto_now_add=False, default=None, null=True)

    def __str__(self):
        return "Message from {}".format(self.guest)

    def save(self, **kwargs):
        super(MessageFromGuest, self).save(**kwargs)
        if self.guest and not self.notified:
            admins = User.objects.filter(is_staff=True).values("email")
            to_email = []
            for admin in admins:
                to_email.append(admin["email"])

            email = EmailMessage(
                f"Nuevo mensaje de {self.guest}",
                self.message,
                settings.DEFAULT_EMAIL_FROM,
                to_email,
                [settings.DEFAULT_EMAIL_FROM],
                reply_to=[self.guest.email],
            )
            email.send()
            self.notified = True
            self.notified_on = now()
            super(MessageFromGuest, self).save(**kwargs)


class Anecdote(models.Model):
    """Messages sent by our guests to us."""

    guest = models.ForeignKey(
        Profile, on_delete=models.SET_NULL, null=True, related_name="messages"
    )
    timestamp = models.DateTimeField(auto_now_add=True)
    message = models.TextField(_("message"), blank=False)

    class Meta:
        get_latest_by = "-timestamp"
        ordering = [
            "-timestamp",
        ]
        verbose_name = _("anecdote")
        verbose_name_plural = _("anecdotes")

    def __str__(self):
        return "Message from {}".format(self.guest)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
