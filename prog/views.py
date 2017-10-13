from django.shortcuts import render



def prog(request):
    return render(request,'prog/prog.html',locals())
