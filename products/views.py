from django.shortcuts import render
from products.models import *

def product(request,product_id):  #ф-ция promoopen принимает request-запррос+product_id из браузера на странице product/1/(напирмер) смотри фаил urls
    product=Product.objects.get(id=product_id)   #передаеться переменная что представляет из себя объект класса продукта(с тем id который передан от браузера)
    return render(request,'products/product.html',locals())
