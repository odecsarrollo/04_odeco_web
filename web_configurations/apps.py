from django.apps import AppConfig


class WebConfigurationsConfig(AppConfig):
    name = 'web_configurations'
    verbose_name = 'Website Configuraciones'

    def ready(self):
        import web_configurations.signals
