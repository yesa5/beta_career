import factory
from sdu_beta_career.users.models import User


class UserFactory(factory.Factory):
    class Meta:
        model = User

    name = factory.Sequence(lambda n: f"user_{n}")
    role = User.ROLES.student
