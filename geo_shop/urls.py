"""geo_shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin

admin.autodiscover()     # Эта функция пытается импортировать модуль admin каждого установленного приложения.
                             #  Предполагается, что в этом модуле выполняется
                              #регистрация моделей в админке.

                                       #django ищет адресс введенныйв браузере localhost:8000/landing/-(после8000)
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('landing.urls')), # include(включить из папки landing  из файла url)
                                        # нужно смотреть адреса в папке landing лежит фаил urls(адрес относительно проекта)

]
