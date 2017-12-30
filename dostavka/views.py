from django.shortcuts import render



def dostavka(request):


    return render(request,'dostavka/dostavka.html',locals())
