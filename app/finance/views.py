from django.shortcuts import render
from .models import Client, Transaction


def clients(request):
    clients = Client.objects.all()
    return render(request, 'finance/clients.html', {'clients': clients})


def transactions(request):
    transactions = Transaction.objects.all()
    return render(request, 'finance/transactions.html', {'transactions': transactions})
