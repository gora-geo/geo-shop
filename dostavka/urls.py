from django.conf.urls import url, include
from dostavka import views

urlpatterns = [
    url(r'^dostavka/', views.dostavka, name='dostavka'),

]
