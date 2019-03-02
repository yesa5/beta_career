from django.test import TestCase
from nose_parameterized import parameterized

from sdu_beta_career.users.factories.profile import ProfileFactory
from sdu_beta_career.users.models import User
from sdu_beta_career.users.models import Profile


class TestProfile(TestCase):
    def setUp(self):
        self.user = User.objects.create(name='Test User')

    def test_create(self):
        Profile.objects.create(user=self.user)

        profiles = Profile.objects.all()
        self.assertEqual(profiles.count(), 1)

    @parameterized.expand([
        (Profile.FACULTIES.engineering, 1),
        (Profile.FACULTIES.law, 2),
        (Profile.FACULTIES.education, 3),
    ])
    def test_faculties(self, faculty: int, expected: int):
        profile = ProfileFactory(faculty=faculty)
        self.assertEqual(profile.faculty, expected)
