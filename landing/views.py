from django.shortcuts import render

def landing(request):  #ф-ция принимает request-запррос из браузера
    name="safonov gora" #вводим перемнную name
    return render(request,'landing/landing.html',locals()) #render выполняет указанный шаблон тоесть отрисовывает его,
                                                            # а ф-ция возврашает его и введеные переменные передает на шаблон
