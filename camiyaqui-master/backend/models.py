from django.contrib.auth.models import User
from django.urls import reverse

from ourwedding.models import Profile

from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.db import models
from django.template import Template, Context
from django.utils.text import slugify

from ourwedding.models import Profile
from ourwedding.tokens import login_token_generator


class Message(models.Model):
    slug = models.SlugField(max_length=255, unique=True)
    language = models.CharField(
        max_length=2, choices=settings.LANGUAGES, null=False, blank=False
    )

    subject = models.CharField(null=False, max_length=255, blank=False)
    template_html = models.TextField(blank=True, null=True)
    template_txt = models.TextField(blank=True)

    def get_absolute_url(self):
        return reverse(
            "message-detail",
            args=[
                self.id,
            ],
        )

    @property
    def sent_to(self):
        sent_to = SentMessages.objects.filter(message=self).distinct()
        return sent_to

    def send(self, guest, context={}, check_language=True):
        if check_language and self.language != guest.profile.language:
            raise Exception(
                "Trying to send a message to {} in {}".format(guest, self.language)
            )

        context.update({"guest": guest})
        context.update({"token": login_token_generator.make_token(guest)})
        context.update({"website": settings.WEBSITE_URL})
        context = Context(context)

        tmpl_txt = Template(self.template_txt)

        msg_txt = tmpl_txt.render(context=context)
        msg = EmailMultiAlternatives(
            self.subject,
            msg_txt,
            settings.EMAIL_FROM,
            [guest.email],
            reply_to=[settings.EMAIL_FROM],
        )
        if self.template_html:
            tmpl_html = Template(self.template_html)
            msg_html = tmpl_html.render(context=context)
            msg.attach_alternative(msg_html, "text/html")

        if SentMessages.objects.filter(sent_to=guest, message=self).exists():
            print(f"Sending message {self.subject} again to {guest}")
        else:
            print(f"Sending message {self.subject} to {guest}")
        msg.send()
        SentMessages.objects.create(message=self, sent_to=guest, text=msg_txt)

    def send_all(self):
        """Send this message to all the users provided that the language is the same.
        It will not send the message twice to the same person.
        """

        users = User.objects.filter(profile__language=self.language)
        i = 0
        for user in users:
            if SentMessages.objects.filter(message=self, sent_to=user).count() == 0:
                self.send(user)
                i += 1
        return i

    def save(self, *args, **kwargs):
        self.slug = slugify(self.subject)
        super(Message, self).save(*args, **kwargs)

    def __str__(self):
        return "{} [{}]".format(self.subject, self.language)


class SentMessages(models.Model):
    """Tracks sent messages, also the text sent."""

    date_sent = models.DateTimeField(auto_now_add=True)
    message = models.ForeignKey(Message, on_delete=models.SET_NULL, null=True)
    sent_to = models.ForeignKey(User, on_delete=models.CASCADE)
    guest = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    text = models.TextField()


class InternalMessage(models.Model):
    """Messages generated internally, for example if someone registers and we need to manually
    verify the information."""

    timestamp = models.DateTimeField(auto_now_add=True)
    message = models.TextField()
    opened = models.BooleanField(default=False)  # If it was viewed on the website
    opened_on = models.DateTimeField(default=None, auto_now_add=False, null=True)
    notified = models.BooleanField(default=False)  # If it was sent by e-mail
    notified_on = models.DateTimeField(auto_now_add=False, default=None, null=True)

    def __str__(self):
        return "Internal Message {}".format(self.message[:120])


class PushTokens(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    token = models.CharField(max_length=255, null=False, blank=False)
    user = models.ForeignKey(
        User,
        related_name="push_token",
        null=True,
        blank=False,
        on_delete=models.CASCADE,
    )
    active = models.BooleanField(default=True)


class Visits(models.Model):
    guest = models.ForeignKey(User, on_delete=models.CASCADE, related_name="visits")
    timestamps = models.DateTimeField(auto_now_add=True)
    page = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.guest.first_name} {self.guest.last_name} - {self.page}"


class News(models.Model):
    language = models.CharField(
        max_length=2, choices=settings.LANGUAGES, null=False, blank=False
    )
    title = models.CharField(max_length=120, blank=False, null=False)
    message = models.TextField()
    published_on = models.DateTimeField(auto_now_add=True)
