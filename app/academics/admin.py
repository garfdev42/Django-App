from django.contrib import admin
from .models import User, Person

# Register your models here.

class UserFields(admin.ModelAdmin):
    list_display = ('email', 'password', 'status')

class PersonFields(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'age', 'ident_number')

admin.site.register(User, UserFields)
admin.site.register(Person, PersonFields)

