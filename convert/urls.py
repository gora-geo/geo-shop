from django.conf.urls import url, include
from django.contrib import admin
from convert import views
from django.conf import settings   #импорт метода settings
from django.conf.urls.static import static #импорт метода sta
urlpatterns = [
    url(r'^convert/', views.convert, name='convert'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

