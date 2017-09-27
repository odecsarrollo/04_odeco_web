from django.apps import AppConfig


class WebSolucionesConfig(AppConfig):
    name = 'web_soluciones'
    verbose_name = 'Website Soluciones'

    def ready(self):
        import web_soluciones.signals
