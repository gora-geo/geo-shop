from django import forms   #импорт модуля forms
from .models import *      #импорт файла models из(*-текушей паки в данном случаее landing)

class CheckoutContactForm(forms.Form):           #создадим класс CheckoutContactForm
    name=forms.CharField(required=True)            #required=True-ключ сообщения об ошибки
    phone=forms.CharField(required=True)
