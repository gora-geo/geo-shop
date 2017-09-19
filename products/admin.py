from django.contrib import admin  #импорт интерфейса администрирования
from .models import *             #импорт файла models из(*-текушей паки в данном случаее landing)

class ProductImageInline(admin.TabularInline): #TabularInlineподкласс InlineModelAdmin(Интерфейс администратора позволяет редактировать связанные объекты на одной странице с родительским объектом. Это называется “inlines”.)
    model = ProductImage
    extra = 0       # Указывает количество пустых форм для добавления объектов в наборе форм.

class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductCategory._meta.fields]

    class Meta:
        model = ProductCategory

admin.site.register(ProductCategory, ProductCategoryAdmin)

class ProductAdmin (admin.ModelAdmin):
    list_display = [field.name for field in Product._meta.fields]
    inlines = [ProductImageInline]    #добовление в данную таблицу в админке (таблицу продукта) таблицы (фотографии продукта)
                                    #тоесть в таблице продукта появиться таблица фотографии и она добавит фотографии при нажати на id или при добовлениии товара
                                #олько для этого надо описать  класс ProductImageInline(как этосделановыше)
    class Meta:
        model = Product

admin.site.register(Product, ProductAdmin)


class ProductImageAdmin (admin.ModelAdmin):
    list_display = [field.name for field in ProductImage._meta.fields]

    class Meta:
        model = ProductImage

admin.site.register(ProductImage, ProductImageAdmin)