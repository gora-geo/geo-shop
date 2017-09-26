from django.http import JsonResponse   #импортируем JsonResponse(которое отдает данныен или ответ в javascript)

def basket_adding(request):   #вводим функцию basket_adding(добовлениев карзину)
    return_dict = dict()   #введем переменную return_dict которая равна пустому словарю,dict()-это фукнукция pythhon которая создает словари
    session_key = request.session.session_key  #введем переменную session_key которая равна  ключю сесии принятому с запроса в браузере
    print (request.POST)   #вывод в терминал содержимого пост запроса(какие данные в пост запросе)
    return JsonResponse(return_dict)  # возврат переменной return_dict(ответный словарь) в javascript