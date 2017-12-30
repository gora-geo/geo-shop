from django.shortcuts import render



def ploh(request):


    return render(request,'ploh/ploh.html',locals())
