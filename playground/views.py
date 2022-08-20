from django.shortcuts import render

# Create your views here.
#it take request and provide response
#request handler
from django.http import HttpResponse

def say_hello(request):
#pull data from db
# transform
#send email and so on
    return render(request,'hello.html',{'name':'sujan'})