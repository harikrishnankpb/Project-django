from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(requests):
    # return HttpResponse("Om Ganesaya namaha")
    return render(requests,'home.html')

def add(requests):
    a=int(requests.POST['a'])
    b=int(requests.POST['b'])
    c=a+b
    return render(requests,'result.html',{'result':c})