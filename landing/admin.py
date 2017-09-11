from django.contrib import admin  #импорт интерфейса администрирования
from .models import *             #импорт файла models из(*-текушей паки в данном случаее landing)

class SubscriberAdmin(admin.ModelAdmin):   #создание класса SubscriberAdmin

    # list_display = ["name","email"]    #говориткакие колонки нужно отображать в в модели(таблице)Subscriber(переименовой в A lot of Subscribers
    list_display = [field.name for field in Subscriber._meta.fields]

    list_filter = ['name',]   #появится фильт справа по имени в котором можно будет выбирать подписчиков по имени
    search_fields = ['name','email']   #появиться фильтр сверху вкотроый можно будет вводить имя или почту и он будет искать пользователей с этим имменем или постой

    #fields = ["email"]  #настройка что поле показываеться

    #exclude = ["email"]  #настройка что поле исключаеться(не показываеться)


    class Meta:                   #доп настройки
        model = Subscriber        #говорит о том чтомы настраиваем модель Subscriber


admin.site.register(Subscriber,SubscriberAdmin)  #регистарация на сайте админки(localhost:8000/admin) модели Subscribers
                                                  # модели SubscriberAdmin
