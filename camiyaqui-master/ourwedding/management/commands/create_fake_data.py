import csv

from django.core.management import BaseCommand
from ourwedding.models import Profile


class Command(BaseCommand):
    args = "filename"

    def add_arguments(self, parser):
        parser.add_argument("filename", nargs="+", type=str)

    def handle(self, filename, *args, **kwargs):
        with open(filename[0], "r") as csv_file:
            reader = csv.reader(csv_file, delimiter=",")
            first_row = True
            for row in reader:
                if first_row:
                    first_row = False
                    continue
                print(row)
                nickname, first_name, last_name, email, language = row[:5]

                if Profile.objects.filter(email=email).count() != 0:
                    print("Skipping {}. Already in list.".format(first_name))
                    continue

                guest = Profile(
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    language=language,
                    nickname=nickname,
                )
                guest.save()
