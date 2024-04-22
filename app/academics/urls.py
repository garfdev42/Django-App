from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("list_persons", views.list_persons, name='list')
]