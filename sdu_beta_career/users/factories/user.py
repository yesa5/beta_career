import factory
from sdu_beta_career.users.models import User


class UserFactory(factory.Factory):
    class Meta:
        model = User

    name = 'John'
    role = User.ROLES.student
