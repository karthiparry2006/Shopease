from django.apps import AppConfig

class ShopeaseConfig(AppConfig):

    default_auto_field = 'django.db.models.BigAutoField'

    name = 'shopease'

    def ready(self):

        import shopease.signals