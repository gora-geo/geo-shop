from django.conf.urls import url, include
from ploh import views

urlpatterns = [
    url(r'^ploh/', views.ploh, name='ploh'),

]
