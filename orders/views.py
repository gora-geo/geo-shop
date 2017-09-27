from django.http import JsonResponse   #импортируем JsonResponse(которое отдает данныен или ответ в javascript)
from .models import *

def basket_adding(request):   #вводим функцию basket_adding(добовлениев карзину)
    return_dict = dict()   #введем переменную return_dict которая равна пустому словарю,dict()-это фукнукция pythhon которая создает словари
    session_key = request.session.session_key  #введем переменную session_key которая равна  ключю сесии принятому с запроса в браузере
    print (request.POST)   #вывод в терминал содержимого пост запроса(какие данные в пост запросе)
    data = request.POST    #содержание пост запроса (объект(словарь) содержаший product_id,nmb,и еще один парамет можно посмотретьв терминале
    product_id = data.get("product_id") #вводим переменную product_id значение которой считываем переменой(словаря)по ключу product_id
    nmb = data.get("nmb")  #аналогично строчке выше
    new_product = ProductInBasket.objects.get_or_create(session_key=session_key, product_id=product_id,
                                                                     is_active=True, nmb=nmb)                #вводим переменную new_product(новый продукт)
                                                                                                             #Удобный метод для поиска объекта по заданным параметрам поиска kwargs, и создания нового при необходимости.
                                                                                                              #Все именованные аргументы переданные в get_or_create() — кроме одного не обязательного defaults — будут использованы при вызове get(). Если объект найден, get_or_create() вернет этот объект и False. Если объект не найден, get_or_create() создаст и сохранит новый объект, возвращая новый объект и True.
    products_in_basket = ProductInBasket.objects.filter(session_key=session_key, is_active=True, order__isnull=True)  #водим переменую  products_in_basket(товар в корзине) куда входят все объекты(список) класса ProductInBasket с сесиое кейм совпадаюшим сполученым выше ,чтобы они были активны,и заказ  был не пуст
    products_total_nmb = products_in_basket.count()  #воодим перемменую products_total_nmb(общее количество)-.count()-метод списка котрый показыает при пустом значение возврашает количество элементов списка
    return_dict["products_total_nmb"] = products_total_nmb #записываем в переменную (словарь)по ключу  products_total_nmb,значение переменой products_total_nmb

    return JsonResponse(return_dict)  # возврат переменной return_dict(ответный словарь) в javascript