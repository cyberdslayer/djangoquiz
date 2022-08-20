from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponse

# Create your views here.
# creating a home function

def home(request):
    return HttpResponse("Hello I am working")

def signup(request):
    return render(request, "authentication/signup.html")

def signin(request):
    return render(request, "authentication/signin.html")

def signout(request):
    pass