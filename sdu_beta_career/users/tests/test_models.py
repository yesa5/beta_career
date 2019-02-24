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
        (User.RoleType.student, 1),
        (User.RoleType.advisor, 2),
        (User.RoleType.approver, 3),
        (User.RoleType.mentor, 4),
    ])
    def test_roles(self, role, expected):
        new_user = User()
        new_user.name = "Test User"
        new_user.role = role
        new_user.save()
        self.assertEquals(new_user.role, expected)
