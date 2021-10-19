from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request,"base.html",{"name":"saikiran"})

def demo(request):
    return HttpResponse("Thank you")
