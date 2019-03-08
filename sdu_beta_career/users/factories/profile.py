import datetime

import factory
from factory.fuzzy import FuzzyFloat, FuzzyInteger, FuzzyDate

from sdu_beta_career.users.factories.user import UserFactory
from sdu_beta_career.users.models import Profile


class ProfileFactory(factory.Factory):
    class Meta:
        model = Profile

    user = UserFactory()
    course = FuzzyInteger(1, 4).fuzz()
    gpa = FuzzyFloat(0.0, 4.0).fuzz()
    birth_date = FuzzyDate(datetime.date(1996, 1, 1), datetime.date(2003, 1, 1)).fuzz()
    linked_in = factory.Sequence(lambda n: f"google.com/user_{n}")

