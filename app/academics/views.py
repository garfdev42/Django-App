from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User
from .forms import UserForm


# Create your views here.
def index(request):
    return HttpResponse("::: Welcome to my site :::")


def list_users(request):
    # return HttpResponse("Here you find a list of users")
    users = User.objects.all()
    return render(request, "academics/list_users.html", {"user": users})


def create_user(request):
    # return HttpResponse("Here you find a list of people")
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("list")
    else:
        form = UserForm()

    return render(request, "academics/create_user.html", {"form": form})
