import json

from io import StringIO

from django.conf import settings
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.core.management import BaseCommand
from django.core.serializers.json import DjangoJSONEncoder


class Command(BaseCommand):
    def handle(self, *args, **options):
        data = list(User.objects.values())
        jsonfile = StringIO()
        jsonfile.write(json.dumps(data, cls=DjangoJSONEncoder))
        message = EmailMessage(
            "Exported Guests",
            "Here is the backup of the guests",
            settings.EMAIL_FROM,
            [settings.EMAIL_FROM],
        )
        message.attach("guests.csv", jsonfile.getvalue(), "text/csv")
        message.send()
