import datetime

from django.core.management.base import BaseCommand, CommandError

from sdu_beta_career.users.models import User, Profile


class Command(BaseCommand):
    help = 'Creates a certain number of users'

    def handle(self, *args, **options):
        try:
            profile_count = int(input('How many profiles should I create: '))
            for count in range(profile_count):
                user = User.objects.create(username="user_{0}".format(count))
                Profile.objects.create(
                    user=user,
                    course=1,
                    gpa=4.0,
                    birth_date=datetime.datetime(2020, 5, 17),
                    linked_in="linkedIn.com/{0}".format(count)
                )

            self.stdout.write(self.style.SUCCESS(
                'Successfully created {0} profiles'.format(profile_count))
            )
        except TypeError:
            raise CommandError('You must write an integer number.')
