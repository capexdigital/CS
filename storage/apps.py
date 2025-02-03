from django.apps import AppConfig

class PdfStorageConfig(AppConfig):  # Note the class name
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'storage'