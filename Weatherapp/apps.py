from django.apps import AppConfig


class WeatherappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Weatherapp'

    def ready(self):
        import Weatherapp.signals  # Import signals when the app is ready
