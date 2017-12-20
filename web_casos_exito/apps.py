from django.apps import AppConfig


class WebCasosExitoConfig(AppConfig):
    name = 'web_casos_exito'
    verbose_name = 'Website Casos Éxito'

    def ready(self):
        import web_casos_exito.signals
