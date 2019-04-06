from django.contrib.postgres.fields import JSONField
from django.db import models

from .config import Policy, Access


class AccessControl(models.Model):
    name = models.CharField(max_length=16)
    controls = JSONField(default=dict)

    def has_access(self, policy: Policy, access: Access) -> bool:
        """Return True if object has right access, otherwise False."""
        return self.controls.get(policy.value, Access.NONE) & access == access

    def can_read(self, policy: Policy) -> bool:
        return self.has_access(policy, Access.READ)

    def can_write(self, policy: Policy) -> bool:
        return self.has_access(policy, Access.WRITE)

    def __str__(self) -> str:
        return self.name
