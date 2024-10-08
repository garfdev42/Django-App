from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("list", views.list_users, name="list"),
    path("create", views.create_user, name="create"),
]
