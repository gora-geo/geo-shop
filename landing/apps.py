# interstore/apps.py
from django.apps import AppConfig

class InterstoreAppConfig(AppConfig):
    name = "landing" # Здесь указываем исходное имя приложения
    verbose_name = "Подписчики" # А здесь, имя которое необходимо отобразить в админке