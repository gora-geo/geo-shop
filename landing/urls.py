from django.conf.urls import url, include
from django.contrib import admin
from landing import views #импотриуем из паки landig фаил views(ф-ция в питоне которая принимает запрос от сервера)

urlpatterns = [
    url(r'^promoopen/', views.promoopen, name='promoopen'), #promoopen/(адрес в браузере-localhost:8000/promoopen/,
                                                      #  в файле views вызываеться ф-ция promoopen

]
