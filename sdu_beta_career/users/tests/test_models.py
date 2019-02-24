import pytest
from django.conf import settings
from django.test import TestCase
from parameterized import parameterized, parameterized_class
from ..models import User
pytestmark = pytest.mark.django_db


def test_user_get_absolute_url(user: settings.AUTH_USER_MODEL):
    assert user.get_absolute_url() == f"/users/{user.username}/"


class TestModelUser(TestCase):
    @parameterized.expand([
        (User.ROLES.student, 0),
        (User.ROLES.advisor, 1),
        (User.ROLES.approver, 2),
        (User.ROLES.mentor, 3),
    ])
    def test_roles(self, role: int, expected: int):
        new_user = User.objects.create(role=role, name='Test User')
        self.assertEquals(new_user.role, expected)
