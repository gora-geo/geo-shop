from django.http import JsonResponse   #импортируем JsonResponse(которое отдает данныен или ответ в javascript)
from .models import ProductInBasket   #импортируем модель ProductInBasket
from django.shortcuts import render

def basket_adding(request):   #вводим функцию basket_adding(добовлениев карзину)
    return_dict = dict()   #введем переменную return_dict которая равна пустому словарю,dict()-это фукнукция pythhon которая создает словари
    session_key = request.session.session_key  #введем переменную session_key которая равна  ключю сесии принятому с запроса в браузере
    print (request.POST)   #вывод в терминал содержимого пост запроса(какие данные в пост запросе)
    data = request.POST    #содержание пост запроса (объект(словарь) содержаший product_id,nmb,и еще один парамет можно посмотретьв терминале
    product_id = data.get("product_id") #вводим переменную product_id значение которой считываем переменой(словаря)по ключу product_id
    nmb = data.get("nmb")  #аналогично строчке выше
    is_delete = data.get("is_delete")   #вводим переменную is_delete значение которой считываем переменой(словаря)по ключу is_delete

    if is_delete == 'true':   #если переменная is_delete принимат значение true
        ProductInBasket.objects.filter(id=product_id).update(is_active=False) #Тогда товары(объекты класса ProductInBasket).меняем(обновляем)их значение is_active=False (тоесть они проппадают из корзины)
    else:                     #иначе если is_delete принимат значение false
        new_product, created = ProductInBasket.objects.get_or_create(session_key=session_key, product_id=product_id,          #вводим переменную new_product(новый продукт)и created(созданный)
                                                                     is_active=True, defaults={"nmb": nmb})   #Если будет находиться по полям session_key,product_id,is_active ничегоне будет меняться если нет то будет исользовать 3 этих поля плюс поле defaults чтобы создать новую запись
                                                                                                             #get_or_create(**kwargs)Удобный метод для поиска объекта по заданным параметрам поиска kwargs, и создания нового при необходимости.
                                                   #если записьь будет создаваться то впишем количество ,а если нет
                                                   #Все именованные аргументы переданные в get_or_create() — кроме одного не обязательного defaults — будут использованы при вызове get(). Если объект найден, get_or_create() вернет этот объект и False. Если объект не найден, get_or_create() создаст и сохранит новый объект, возвращая новый объект и True.
        if not created:
            print ("not created")     #вывод в терминал слова not created
            new_product.nmb += int(nmb)    #количесто нового продукта = старое количество+количество толькочто введеного
            new_product.save(force_update=True)  #обновление записи (замешение предыдущегозначения)





    products_in_basket = ProductInBasket.objects.filter(session_key=session_key, is_active=True, order__isnull=True)  #водим переменую  products_in_basket(товар в корзине) куда входят все объекты(список) класса ProductInBasket с сесиое кейм совпадаюшим сполученым выше ,чтобы они были активны,и заказ  был не пуст
    products_total_nmb = products_in_basket.count()                #воодим перемменую products_total_nmb(общее количество)-.count()-метод списка котрый показыает при пустом значение возврашает количество элементов списка
    return_dict["products_total_nmb"] = products_total_nmb          #добовление в словарь return_dict по ключу products_total_nmb значения products_total_nmb
    return_dict["products"] = list()                                #добовление в словарь return_dict по ключу products путого списка  list()
    for item in  products_in_basket:                                #начинаем перебор объектов входящих в products_in_basket
        product_dict = dict()                                         #вводим перемменую product_dict(словарь) и присваиваем ей значениее пустой только что созданный словарь
        product_dict["id"] = item.id                                   #в словарь  product_dict по ключу id добовляем значение id объекта класса  ProductInBasket
        product_dict["name"] = item.product.name       #в словарь  product_dict по ключу name добовляем значение product.name объекта класса  ProductInBasket
        product_dict["price_per_item"] = item.price_per_item #в словарь  product_dict по ключу price_per_item добовляем значение price_per_item объекта класса  ProductInBasket
        product_dict["nmb"] = item.nmb       #в словарь  product_dict по ключу id добовляем значение id объекта класса  ProductInBasket
        return_dict["products"].append(product_dict)    #в словарь return_dict по ключу products добовление перемменой(словаря) product_dict
        return_dict["products_total_nmb"] = products_total_nmb #записываем в переменную (словарь)по ключу  products_total_nmb,значение переменой products_total_nmb

    return JsonResponse(return_dict)  # возврат переменной return_dict(ответный словарь) в javascript


def checkout(request):         #вводим функцию checkout(проверка)

    session_key = request.session.session_key             #вводим переменную session_key = ключу сесии от браузера
    products_in_basket = ProductInBasket.objects.filter(session_key=session_key, is_active=True)    #вводим переменную products_in_basket(товары в к
    print (products_in_basket)                   #выводим переменную products_in_basket в терминал

    return render(request, 'orders/checkout.html', locals())   #render выполняет указанный шаблон тоесть отрисовывает его,orders/checkout.html-путь до файла html в templates
                                                                   # а ф-ция возврашает его и введеные переменные передает на шаблон