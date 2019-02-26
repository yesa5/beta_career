from django.test import TestCase
from sdu_beta_career.users.models import User
from sdu_beta_career.users.models import Profile


class TestProfile(TestCase):
    def setUp(self):
        self.user = User.objects.create(name='Test User')

    def test_create(self):
        Profile.objects.create(user=self.user)

        profiles = Profile.objects.all()
        self.assertEquals(profiles.count(), 1)
