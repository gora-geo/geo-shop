from django.contrib import admin  #импорт интерфейса администрирования
from .models import *             #импорт файла models из(*-текушей паки в данном случаее landing)

class ProductInOrderInline(admin.TabularInline):#TabularInline подкласс InlineModelAdmin(Интерфейс администратора позволяет редактировать связанные объекты на одной странице с родительским объектом. Это называется “inlines”.)
    model = ProductInOrder
    extra = 0     # Указывает количество пустых форм для добавления объектов в наборе форм.

class StatusAdmin (admin.ModelAdmin):                              #при описание это класса
    list_display = [field.name for field in Status._meta.fields]   #в админке создаеться таблица Satus



    class Meta:
        model = Status

admin.site.register(Status, StatusAdmin)



class OrderAdmin (admin.ModelAdmin):#создает таблицу в админке (заказ(в order)
    list_display = [field.name for field in Order._meta.fields]
    inlines = [ProductInOrderInline]   #в таблице заказ появиться внизу таблица товар в заказе

    class Meta:
        model = Order

admin.site.register(Order, OrderAdmin)


class ProductInOrderAdmin (admin.ModelAdmin):  #создает таблицу в админке (товар в заказе(в order)
    list_display = [field.name for field in ProductInOrder._meta.fields]

    class Meta:
        model = ProductInOrder


admin.site.register(ProductInOrder, ProductInOrderAdmin)


class ProductInBasketAdmin (admin.ModelAdmin):  #создает таблицу в админке (товар в корзине(в order)
    list_display = [field.name for field in ProductInBasket._meta.fields]  #делает видимыми все поля

    class Meta:                       #доп настройки
        model = ProductInBasket        #оворит о том что мы настри ваем модель ProductInBasket

admin.site.register(ProductInBasket, ProductInBasketAdmin)  #регистарация на сайте админки(localhost:8000/admin) в таблице(модели)  ProductInBasket таблицы(модели)ProductInBasketAdmin