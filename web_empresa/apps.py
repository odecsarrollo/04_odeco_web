from django.apps import AppConfig


class WebEmpresaConfig(AppConfig):
    name = 'web_empresa'
    verbose_name = 'Website Empresa'

    def ready(self):
        import web_empresa.signals
