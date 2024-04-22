from django.shortcuts import render
from django.http import HttpResponse
from .models import User

# Create your views here.
def index(request):
    return HttpResponse("::: Welcome to my site :::")

def list_users(request):
    #return HttpResponse("Here you find a list of users")
    users = User.objects.all()
    return render(request, 'academics/list_users.html',{'user':users})

def create_user(request):
    return HttpResponse("Here you find a list of people")