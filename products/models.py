from django.db import models  #импорт приложения models

class ProductCategory(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = 'Категория товара'
        verbose_name_plural = 'Категория товаров'

class Product(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True, default=None,verbose_name='Имя')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0,verbose_name='цена')
    discount = models.IntegerField(default=0,verbose_name='Скидка')
    category = models.ForeignKey(ProductCategory, blank=True, null=True, default=None)
    short_description = models.TextField(blank=True, null=True, default=None,verbose_name='кроткое описание')
    description = models.TextField(blank=True, null=True, default=None,verbose_name='Описание')
    is_active = models.BooleanField(default=True,verbose_name='Активный')
    created = models.DateTimeField(auto_now_add=True, auto_now=False,verbose_name='создан')
    updated = models.DateTimeField(auto_now_add=False, auto_now=True,verbose_name='обновлен')

    def __str__(self):
        return "%s, %s" % (self.price, self.name)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

class ProductImage(models.Model):
    product = models.ForeignKey(Product, blank=True, null=True, default=None,verbose_name='продукт')
    image = models.ImageField(upload_to='products_images/',verbose_name='Картинка')  #путь к картинке в папек static/products_images/
    is_main=models.BooleanField(default=False,verbose_name='Главная')   #поле модели(таблицы)-главная тоест какая картинка если их несколько будет выводиться первой
    is_active = models.BooleanField(default=True,verbose_name='активный')  #активна ли картинка
    created = models.DateTimeField(auto_now_add=True, auto_now=False,verbose_name='создан')
    updated = models.DateTimeField(auto_now_add=False, auto_now=True,verbose_name='обновлен')

    def __str__(self):
        return "%s" % self.id #настраивает отображение в таблице (home/productss/product(потомA lot of orderss)id( продукта)

    class Meta:                        #доп настройки для модели
        verbose_name = 'Фотография'         #Читабельное название модели, в единственном числе:
        verbose_name_plural = 'Фотографии'   #Название модели в множественном числ (админка будет выгладить products/фотографии/если добавить и вверху-фотография

