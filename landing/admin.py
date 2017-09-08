from django.contrib import admin  #импорт интерфейса администрирования
from .models import *             #импорт файла models из(*-текушей паки в данном случаее landing)
admin.site.register(Subscribers)  #регистарация на сайте админки(localhost:8000/admin) модели Subscribers
