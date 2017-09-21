from django.conf.urls import url, include
from django.contrib import admin
from landing import views #импотриуем из паки landig фаил views(ф-ция в питоне которая принимает запрос от сервера)
from django.conf import settings   #импорт метода settings
from django.conf.urls.static import static #импорт метода static
urlpatterns = [
    url(r'^$', views.home, name='home'), #r'^$'-адресс страницы localhost:8000  #  в файле views вызываеться ф-ция home
    url(r'^promoopen/', views.promoopen, name='promoopen'), #promoopen/(адрес в браузере-localhost:8000/promoopen/,
                                                      #  в файле views вызываеться ф-ция promoopen

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

#нужно чтобы добвлялись картнки из static/media