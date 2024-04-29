from django.contrib import admin

# Register your models here.
from .models import Client, Client_Product, Product, Transaction, TransactionType

admin.site.register(Client)
admin.site.register(Product)
admin.site.register(Client_Product)
admin.site.register(TransactionType)
admin.site.register(Transaction)
