from django.db import models
# Create your models here.
import datetime

#Va indentado principalemte tabulacion 
#model.DateTimeField(auto_now=True, null=False) =>
#model.DateTimeField() 


class User(models.Model):
    email = models.EmailField(null = True, blank = True)
    password = models.CharField(null = True, blank = True)
    status = models.BooleanField(null = True, blank = True, default = True)
    created_at = models.DateTimeField(default=datetime.datetime.now())
    updated_at = models.DateTimeField(default=datetime.datetime.now())
    deleted_at = models.DateTimeField(null = True, blank = True)

class Person(models.Model):
     firstname = models.CharField(max_length = 20)
     lastname = models.CharField(max_length=20)
     age = models.IntegerField()
     ident_number = models.CharField(max_length=12, blank=True)
     created_at = models.DateTimeField(default=datetime.datetime.now())
     updated_at = models.DateTimeField(default=datetime.datetime.now())
     deleted_at = models.DateTimeField(null = True, blank = True)
