# interstore/apps.py
from django.apps import AppConfig

class InterstoreAppConfig(AppConfig):
    name = "products" # Здесь указываем исходное имя приложения
    verbose_name = "Продукты" # А здесь, имя которое необходимо отобразить в админке