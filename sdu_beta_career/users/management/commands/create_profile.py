import datetime
import random

from django.core.management.base import BaseCommand, CommandError

from sdu_beta_career.users.models import User, Profile


class Command(BaseCommand):
    help = 'Creates a certain number of users'

    def handle(self, *args, **options):
        try:
            profile_count = int(input('How many profiles should I create: '))
            for count in range(profile_count):
                user = User.objects.create(username=f"user_{count}")
                Profile.objects.create(
                    user=user,
                    course=random.randint(1, 5),
                    gpa=round(random.uniform(0, 5), 2),
                    birth_date=datetime.datetime(2020, 5, 17),
                    linked_in=f"linkedIn.com/{count}"
                )

            self.stdout.write(self.style.SUCCESS(
                f'Successfully created {profile_count} profiles')
            )
        except TypeError:
            raise CommandError('You must write an integer number.')
