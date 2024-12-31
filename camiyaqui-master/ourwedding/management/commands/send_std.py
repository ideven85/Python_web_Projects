from optparse import make_option
from django.core.management import BaseCommand

from communications.models import Message
from ourwedding.models import Profile
from ourwedding.save_the_date import save_the_date_test


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument(
            "--repeat",
            action="store_true",
            dest="send",
            default=False,
            help="Send again to all contacts",
        )
        parser.add_argument(
            "msg",
            help="Mark as sent",
            type=int,
        )
        parser.add_argument(
            "--reset",
            action="store_true",
            dest="reset",
            default=False,
            help="Reset sent flags",
        )

    def handle(self, *args, **options):
        msg = Message.objects.get(pk=options["msg"])
        guests = Profile.objects.filter(language=msg.language)
        for guest in guests:
            msg.send(guest, {})
            print(guest)
