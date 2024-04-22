from django.db import models
import datetime

#model.DateTimeField(auto_now=True, null=False) => updated_at
#model.DateTimeField(auto_now_add=True, null=False) => Default now()

# Create your models here.
class DateTimeModel(models.Model):
    created_at = models.DateTimeField(default=datetime.datetime.now())
    updated_at = models.DateTimeField(default=datetime.datetime.now())
    deleted_at = models.DateTimeField(null = True, blank = True)

    class Meta:
        abstract = True

class Person(DateTimeModel):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    age = models.IntegerField()
    ident_number = models.CharField(max_length=12, blank=True)
    id_user = models.ForeignKey('User', on_delete = models.CASCADE, blank=False, null=False, default=1)

class User(DateTimeModel):
    email = models.EmailField(null = True, blank = True)
    password = models.CharField(null = True, blank = True)
    status = models.BooleanField(null = True, blank = True, default = True)

    #def __str__(self):
    #    return f"{self.email} - {self.password}"

