from django.db import models  #импорт приложения models
from products .models import Product #импортируе модуль Product чтобыработала строка  product = models.ForeignKey(Product, blank=True, null=True, default=None)
from django.db.models.signals import post_save   #импрот метода save(после нажати кнопки в админке)

class Status(models.Model):
    name = models.CharField(max_length=24, blank=True, null=True, default=None,verbose_name='статус заказа')
    is_active = models.BooleanField(default=True,verbose_name='Активный')
    created = models.DateTimeField(auto_now_add=True, auto_now=False,verbose_name='Создан')
    updated = models.DateTimeField(auto_now_add=False, auto_now=True,verbose_name='Обновленен')

    def __str__(self):
        return "Статус %s" % self.name

    class Meta:
        verbose_name = 'Статус заказа'
        verbose_name_plural = 'Статусы заказа'

class Order(models.Model):#создание класса Order наслед.от Model-создает таблицу в базе данных
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)#total price for all products in order
    customer_name = models.CharField(max_length=64, blank=True, null=True, default=None,verbose_name='Имя заказчика') #тоесть Orders модель создаст в бвзе данных таблицу с полями customer_name CharField-так мы определяем текстовое поле с ограничением на количество символов.
    customer_phone = models.CharField(max_length=48, blank=True, null=True, default=None,verbose_name='Телефон заказчика')#blank=True,проверка данных в форме позволит сохранять пустое значение в поле. При blank=False поле будет обязательным.
    customer_address = models.CharField(max_length=128, blank=True, null=True, default=None,verbose_name='Адрес заказчика')#max_length=128 - макс длина поля 128,null=True-Django сохранит пустое значение как NULL в базе данных
    comments = models.TextField(blank=True, null=True, default=None,verbose_name='Коментраии')#default=None-значение по умолчанию для поля None-тоесть ничего
    status = models.ForeignKey(Status,verbose_name='Статус')#models.ForeignKey -- ссылка на другую модель-(Status)
    created = models.DateTimeField(auto_now_add=True, auto_now=False,verbose_name='Создан') #auto_now_add=True-Значение поля будет автоматически установлено в текущую дату при создании(первом сохранении) объекта.
                                                                      #TextField -- так определяется поле для неограниченно длинного текста. Выглядит подходящим для содержимого поста
    updated = models.DateTimeField(auto_now_add=False, auto_now=True,verbose_name='Обновлен') #auto_now=True-Значение поля будет автоматически установлено в текущую дату при каждом сохранении объекта.
                                                                       #models.DateTimeField -- дата и время
    def __str__(self):
        return "Заказ %s %s" % (self.id,self.status.name)   #настраивает отображение в таблице (home/orders/order(потомA lot of orderss) строки подписчиков(заказ-id(заказа),и имя сатуса(тоесть поле name объекта класса status)



    class Meta:                          #доп настройки для модели
        verbose_name = 'Заказ'           #Читабельное название модели, в единственном числе:
        verbose_name_plural = 'Заказы'     #Название модели в множественном числ (админка будет выгладить orders/заказы/если добавить и вверху-заказ

    def save(self, *args, **kwargs):  #переопределеие save в таблице заказы

        super(Order, self).save(*args, **kwargs)

class ProductInOrder(models.Model):  #создание класса ProductInOrder наслед.от Model-создает таблицу в базе данных
    order = models.ForeignKey(Order, blank=True, null=True, default=None,verbose_name='Заказ')  #models.ForeignKey -- ссылка на другую модель-(Order)
    product = models.ForeignKey(Product, blank=True, null=True, default=None,verbose_name='Продукт')  #models.ForeignKey -- ссылка на другую модель-(Product)
    nmb = models.IntegerField(default=1,verbose_name='Номер')  #IntegerField(default=1) -числовое поле значение по умолчанию 1
    price_per_item = models.DecimalField(max_digits=10, decimal_places=2, default=0,verbose_name='Цена')  #DecimalField-Десятичное число с фиксированной точностью max_digits=10-Максимальное количество цифр в числе. =10 decimal_places=2- Количество знаков после запятой.default=0-значенре по умолчанию 0
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0,verbose_name='Общая цена')#price*nmb
    is_active = models.BooleanField(default=True,verbose_name='активный')
    created = models.DateTimeField(auto_now_add=True, auto_now=False,verbose_name='Создан')
    updated = models.DateTimeField(auto_now_add=False, auto_now=True,verbose_name='обновлен')

    def __str__(self):
        return "%s" % self.product.name     #настраивает отображение в таблице (home/orders/order(потомA lot of orderss) строки подписчиков(название продукта)

    class Meta:                                   #доп настройки для модели
        verbose_name = 'Товар в заказе'           #Читабельное название модели, в единственном числе:
        verbose_name_plural = 'Товары в заказе'   #Название модели в множественном числ (админка будет выгладить orders/Товары в заказе/если добавить и вверху-Товар в заказе



    def save(self, *args, **kwargs):     #переопределение метода save тоесть,оесть что будет выполняться при нажатии save в таблице товар в заказе
        price_per_item = self.product.price   #читывание цены товара
        self.price_per_item = price_per_item
        print(self.nmb)
        self.total_price = int(self.nmb) * price_per_item  #умножение получение цены товара на количество товара общей цены

        super(ProductInOrder, self).save(*args, **kwargs)

def product_in_order_post_save(sender, instance, created, **kwargs):  #фция товар в заказе после нажатия save
    order = instance.order  #создание экземпляра класса заказ
    all_products_in_order = ProductInOrder.objects.filter(order=order) #выводяться все товары в данном заказе

    order_total_price = 0
    for item in all_products_in_order:
        order_total_price += item.total_price    #подсчет общей сумы заказа

    instance.order.total_price = order_total_price
    instance.order.save(force_update=True)


post_save.connect(product_in_order_post_save, sender=ProductInOrder)  #сохраниене  общей цены товар(в модели)товар в заказе