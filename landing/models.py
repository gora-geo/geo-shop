from django.db import models  #импорт приложения models

class Subscriber(models.Model):  #создание класса Subscribers наслед.от Model-создает таблицу в базе данных
    email = models.EmailField(verbose_name='Почта')       #тоесть Subscribers модель создаст в бвзе данных таблицу с полями email и  name verbose_name='Почта' отображение в админке
    name = models.CharField(max_length=125,verbose_name='Имя')  #max_length=125 - макс длина поля 125 verbose_name='Имя'-отображениевадминке

    def __str__(self):
        return "Пользователь %s %s" % (self.email,self.name)  #настраивает отображение в таблице (home/landing/subscribe(потомA lot of Subscribers) строки подписчиков(пользователь-почта(подписчика) имя(подписчика)

    class Meta:                          #доп настройки для модели
        verbose_name="Мои подписчики"       #Читабельное название модели, в единственном числе:
        verbose_name_plural="Все подписчики"  #Название модели в множественном числ (админка будет выгладить landing/Все подписчкики/если добавить и вверхуМои подписчики
