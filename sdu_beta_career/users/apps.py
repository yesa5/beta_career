from django.apps import AppConfig


class UsersAppConfig(AppConfig):
    name = "sdu_beta_career.users"
    verbose_name = "Users"

    def ready(self):
        from . import signals
