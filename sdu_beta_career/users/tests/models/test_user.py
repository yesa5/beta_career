from django.test import TestCase
from parameterized import parameterized
from sdu_beta_career.users.models import User


class TestUser(TestCase):
    @parameterized.expand([
        (User.ROLES.student, 1),
        (User.ROLES.advisor, 2),
        (User.ROLES.approver, 3),
        (User.ROLES.mentor, 4),
    ])
    def test_roles(self, role: int, expected: int):
        new_user = User.objects.create(role=role, name='Test User')
        self.assertEquals(new_user.role, expected)
