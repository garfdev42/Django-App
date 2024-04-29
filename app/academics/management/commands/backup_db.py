from django.core.management.base import BaseCommand 

#from django.contrib.auth.models import Users
from academics.models import User

import json 


class Command(BaseCommand):
    help = 'Make a database backup in JSON FORMAT'

    def handle(self,*args, **options):
        #Get data from user Model
        users =  User.objects.all()

        #Convert data to dicctionaries 
        data = [{ 
            'email': user.email,
            'password': user.password,
            'status': user.status
         }
         for user in users
         ]
        
        with open('backup_db,json','w') as file:
            json.dump(data,file, indent =4)
         
























