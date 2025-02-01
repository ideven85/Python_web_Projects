import datetime

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    host = request.META.items()
    response = HttpResponse()
    response.set_cookie('my_cookie','temp')


    return render(request,'index.html')
