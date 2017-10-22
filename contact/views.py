from django.shortcuts import render
from products.models import *


def contact(request):
    return render(request,'contact/contact.html',locals())
