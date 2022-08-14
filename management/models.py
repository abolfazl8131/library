from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser , BaseUserManager
import enum
from django.utils.translation import gettext_lazy as _
from datetime import date
# Create your models here.

class LibraryAdminManager(BaseUserManager):
    
    def create_user(self, email , password , **extra_fields ):

        print(1111111111111111111111)
      
        user = self.model(
            
            admin_email = self.normalize_email(extra_fields['admin_email']),
            admin_ID = extra_fields['admin_ID'] , 
            admin_first_name = extra_fields['admin_first_name'] , 
            admin_last_name = extra_fields['admin_last_name'] , 
            admin_birth_date = extra_fields['admin_birth_date'] , 
            admin_date_joined = extra_fields['admin_date_joined'] , 
            admin_date_left = extra_fields['admin_date_left'] , 
            admin_left = extra_fields['admin_left'] , 
            admin_phone_number = extra_fields['admin_phone_number'] , 
            admin_position = extra_fields['admin_position'] , 
           

        )
        user.set_password(extra_fields['admin_ID'])
        user.save()
        return user

    




class Position(models.TextChoices):
    MASTER = 'MS', _('Master')
    CASHIER = 'CA', _('Cashier')
    CLERK = 'CL', _('Clerk')
        


class LibraryAdmin(AbstractBaseUser):
  
    admin_ID = models.CharField(max_length=100, unique=True, db_index=True , default='SOME STRING')
    admin_first_name = models.CharField(max_length=100 , default='SOME STRING')
    admin_last_name = models.CharField(max_length=100 , default='SOME STRING')
    admin_birth_date = models.DateField(null=True)
    admin_date_joined = models.DateField(null=True)
    admin_date_left = models.DateField(null=True)
    admin_left = models.BooleanField(default=False)
    admin_email = models.EmailField(default='SOME@STRING')
    admin_phone_number = models.CharField(max_length=100 ,default='SOME STRING')
    admin_position = models.CharField(max_length=2, choices=Position.choices, default=Position.CLERK)
    admin_is_active = models.BooleanField(default=True)

   

    USERNAME_FIELD = 'admin_ID'

    objects = LibraryAdminManager()

    def get_position(self):
        return self.admin_position

    def leave(self):
        self.admin_left = True
        self.admin_date_left =  date.today()

    
   
