import pytest
from django.conf import settings
from django.test import TestCase
from ..models import User
pytestmark = pytest.mark.django_db


def test_user_get_absolute_url(user: settings.AUTH_USER_MODEL):
    assert user.get_absolute_url() == f"/users/{user.username}/"


class TestModelUser(TestCase):
    def test_default_user(self):
        new_user = User()
        new_user.name = "Test User"
        new_user.save()
        self.assertEqual(new_user.role, 1)

    def test_advisor_user(self):
        new_user = User()
        new_user.name = "Test User"
        new_user.role = 2
        new_user.save()
        self.assertEqual(new_user.role, 2)

    def test_mentor_user(self):
        new_user = User()
        new_user.name = "Test User"
        new_user.role = 4
        new_user.save()
        self.assertEqual(new_user.role, 4)

    def test_approve_user(self):
        new_user = User()
        new_user.name = "Test User"
        new_user.role = 3
        new_user.save()
        self.assertEqual(new_user.role, 3)
