from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homepage(request):
    return HttpResponse("<h1>welcome aboard</h1>")

def page2(request):
    return render(request,'home.html')