from django.db import models
from django.contrib.auth.hashers import make_password


class Client(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    mobile = models.CharField(max_length=50)
    password = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        super(Client, self).save(*args, **kwargs)

    def __str__(self):
        return self.first_name + ' ' + self.last_name + ' - ' + self.email + ' - ' + self.mobile


class Product(models.Model):
    name = models.CharField(max_length=100)
    abbreviation = models.CharField(max_length=10)
    description = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name + ' (' + self.abbreviation + ')' + ' - ' + self.description


class Client_Product(models.Model):
    id_client = models.ForeignKey(Client, on_delete=models.CASCADE)
    id_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    account_number = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.id_client.first_name + ' ' + self.id_client.last_name + ' - ' + self.id_product.name


class TransactionType(models.Model):
    name = models.CharField(max_length=50)
    abbreviation = models.CharField(max_length=10)
    description = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name + ' (' + self.abbreviation + ')' + ' - ' + self.description


class Transaction(models.Model):
    id_client_product = models.ForeignKey(
        Client_Product, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    id_transaction_type = models.ForeignKey(
        TransactionType, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.id_client_product.id_client.first_name + ' ' + self.id_client_product.id_client.last_name + ' ' + self.id_client_product.id_product.name + ' - ' + self.id_transaction_type.name + ' - ' + str(self.amount)
