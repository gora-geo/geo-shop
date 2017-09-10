from django.db import models  #импорт приложения models

class Subscriber(models.Model):  #создание класса Subscribers наслед.от Model-создает таблицу в базе данных
    email = models.EmailField()       #тоесть Subscribers модель создаст в бвзе данных таблицу с полями email и  name
    name = models.CharField(max_length=125)  #max_length=125 - макс длина поля 125

    def __str__(self):
        return "Пользователь %s %s" % (self.email,self.name)  #настраивает отображение в таблице (home/landing/subscribe(потомA lot of Subscribers) строки подписчиков(пользователь-почта(подписчика) имя(подписчика)

    class Meta:                          #доп настройки для модели
        verbose_name="MySubscriber"       #Читабельное название модели, в единственном числе:
        verbose_name_plural="A lot of Subscribers"  #Название модели в множественном числ (админка будет выгладить landing/A lot of Subscribers/если добавить и вверхуMySubscriber
