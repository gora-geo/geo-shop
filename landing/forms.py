from django import forms   #импорт модуля forms
from .models import *      #импорт файла models из(*-текушей паки в данном случаее landing)

class SubscriberForm(forms.ModelForm):   #создание класса SubscriberForm от род.ModelForm(тоесть создание модели формы)тоесть создаеться форма
    class Meta:                          #настройка модели
        model = Subscribers              #модель формы(форма) на основе модели Subscribers(  создаеться из полей в Subscribers)
        exclude = [""]                   #обязательный параметр указывает какае поля стоит исключить
