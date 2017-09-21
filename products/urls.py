from django.conf.urls import url, include
from django.contrib import admin
from products import views

urlpatterns = [
    url(r'^product/(?P<product_id>\w+)/$', views.product, name='product'),  #product/(?P<product_id>\w+)/$(адрес в браузере-localhost:8000/product/1(или другое число номер id),
                                                      #  в файле views вызываеться ф-ция product
]
