from django.apps import AppConfig

class IptalConfig(AppConfig):
    name = 'iptal'

    def ready(self):
        import iptal.signals   # signals modülünü register et
