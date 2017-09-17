from django.shortcuts import render
from .forms import SubscriberForm   #импорт формы SubscriberForm
from products.models import *

def promoopen(request):  #ф-ция promoopen принимает request-запррос из браузера на странице promoopen/ смотри фаил urls
    name="safonov gora" #вводим перемнную name

    form = SubscriberForm(request.POST or None)   #создание объеката классаSubscriberForm(тоесть формы с полями как Subscribers
    if request.method == "POST" and form.is_valid(): #если ответ с формы (в браузере с пост обработкой(<form action="" method = "post">)) и форма прошла валидацию что тип данных вводимых совпадает
        print(form)  #вывод terminal формы
        print(form.cleaned_data)  #вывод cleaned_data(чистых данных формы)-почту,имя
        data = form.cleaned_data
        print(data["name"])    #вывод только имени
        print(form.cleaned_data["name"]) #вывод только имени
        new_form=form.save()  # save(). Этот метод создаёт и сохраняет объект в базе данных, используя для этого данные, введённые в форму.
    return render(request,'landing/landing.html',locals()) #render выполняет указанный шаблон тоесть отрисовывает его,
                                                            # а ф-ция возврашает его и введеные переменные передает на шаблон

def home(request): #ф-ция home принимает request-запррос из браузера
    products_images=ProductImage.objects.filter(is_active=True,is_main=True)  #переменая куда входят все объеты класса ProductImage c галками активный и главная

    return render(request, 'landing/home.html', locals())  #ответ на request отрисовка страница передача перемееной