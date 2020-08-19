from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request): # A view
    return render(request,"hello/index.html")

def brian(request): #Another veiw
    return HttpResponse("Hello Brian!!")

def greet(request,name):
    return render(request,"hello/greet.html",{
        "name":name.capitalize()
    })