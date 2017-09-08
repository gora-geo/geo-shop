from django.db import models  #импорт приложения models

class Subscribers(models.Model):  #создание класса Subscribers наслед.от Model-создает таблицу в базе данных
    email = models.EmailField()       #тоесть Subscribers модель создаст в бвзе данных таблицу с полями email и  name
    name = models.CharField(max_length=125)  #max_length=125 - макс длина поля 125
