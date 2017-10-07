from .models import ProductInBasket  #импорт модели ProductInBasket

def getting_basket_info(request):    #вводим функцию контект-процессора
    session_key = request.session.session_key    #вводим перемменую session_key в ответ с браузера
    if not session_key:                          #если нет ключа сесии(..._)
        request.session["session_key"] = 123
        request.session.cycle_key()                 #(...)создает его



    products_in_basket = ProductInBasket.objects.filter(session_key=session_key, is_active=True, order__isnull=True)   #вводим пееременую products_in_basket(товары в корзине),это объекты класса ProductInBasket,по данному ключу сссеии активные ,,и заказ  был не пуст
    products_total_nmb = products_in_basket.count()      #вводим перемменую products_total_nmb(количество товаров) .count()-количество элементов в списке

    return locals()     #возврашаем в локале локал есть все переменные и функция
