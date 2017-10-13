from django.conf.urls import url, include
from prog import views

urlpatterns = [
    url(r'^prog/', views.prog, name='prog'),

]
