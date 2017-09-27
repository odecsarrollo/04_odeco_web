from django.apps import AppConfig


class WebClientesConfig(AppConfig):
    name = 'web_clientes'
    verbose_name = 'Website Clientes'

    def ready(self):
        import web_clientes.signals
