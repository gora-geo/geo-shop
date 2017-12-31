# interstore/apps.py
from django.apps import AppConfig

class InterstoreAppConfig(AppConfig):
    name = "orders" # Здесь указываем исходное имя приложения
    verbose_name = "Заказы" # А здесь, имя которое необходимо отобразить в админке