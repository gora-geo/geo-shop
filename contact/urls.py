from django.conf.urls import url, include
from contact import views

urlpatterns = [
    url(r'^contact/', views.contact, name='contact'),

]
