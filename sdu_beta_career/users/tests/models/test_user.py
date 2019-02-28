from django.test import TestCase
from parameterized import parameterized

from sdu_beta_career.users.factories.user import UserFactory
from sdu_beta_career.users.models import User


class TestUser(TestCase):
    @parameterized.expand([
        (User.ROLES.student, 1),
        (User.ROLES.advisor, 2),
        (User.ROLES.approver, 3),
        (User.ROLES.mentor, 4),
    ])
    def test_roles(self, role: int, expected: int):
        user = UserFactory(role=role)
        self.assertEquals(user.role, expected)
