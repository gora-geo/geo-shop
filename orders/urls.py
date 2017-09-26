from django.conf.urls import url, include
from django.contrib import admin
from . import views   #импорт  файла views(orders0


urlpatterns = [
    url(r'^basket_adding/$', views.basket_adding, name='basket_adding'),   #basket_adding/(адрес в браузере-localhost:8000/basket_adding/,
                                                                   #  в файле views вызываеться ф-ция basket_adding

]
