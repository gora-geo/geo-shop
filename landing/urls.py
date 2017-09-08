from django.conf.urls import url, include
from django.contrib import admin
from landing import views #импотриуем из паки landig фаил views(ф-ция в питоне которая принимает запрос от сервера)

urlpatterns = [
    url(r'^landing/', views.landing, name='landing'), #landing/(адрес в браузере-localhost:8000/landing/,
                                                      #  в файле views вызываеться ф-ция landing

]
