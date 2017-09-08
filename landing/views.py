from django.shortcuts import render
from .forms import SubscriberForm   #импорт формы SubscriberForm

def landing(request):  #ф-ция принимает request-запррос из браузера
    name="safonov gora" #вводим перемнную name

    form = SubscriberForm(request.POST or None)   #создание объеката классаSubscriberForm(тоесть формы с полями как Subscribers
    if request.method == "POST" and form.is_valid(): #если ответ с формы (в браузере с пост обработкой(<form action="" method = "post">)) и форма прошла валидацию что тип данных вводимых совпадает
        print(form)  #вывод terminal формы
        print(form.cleaned_data)
        data = form.cleaned_data
        print(data["name"])
        print(form.cleaned_data["name"])
        new_form=form.save()
    return render(request,'landing/landing.html',locals()) #render выполняет указанный шаблон тоесть отрисовывает его,
                                                            # а ф-ция возврашает его и введеные переменные передает на шаблон
