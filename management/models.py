from http import server
from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser , BaseUserManager
import enum
from django.utils.translation import gettext_lazy as _
from datetime import date
# Create your models here.

class LibraryAdminManager(BaseUserManager):
    
    def create_user(self, email , password , **extra_fields ):

        user = self.model(
            
            admin_email = self.normalize_email(extra_fields['email']),
            **extra_fields 

        )
        user.set_password(extra_fields['ID'])
        user.save()
        return user

    
    




class Position(models.TextChoices):
    MASTER = 'MS', _('Master')
    CASHIER = 'CA', _('Cashier')
    CLERK = 'CL', _('Clerk')
        


class LibraryAdmin(AbstractBaseUser):
  
    ID = models.CharField(max_length=100, unique=True, db_index=True , default='SOME STRING')
    first_name = models.CharField(max_length=100 , default='SOME STRING')
    last_name = models.CharField(max_length=100 , default='SOME STRING')
    birth_date = models.DateField(null=True)
    date_joined = models.DateField(null=True)
    date_left = models.DateField(null=True)
    left = models.BooleanField(default=False)
    email = models.EmailField(default='SOME@STRING')
    phone_number = models.CharField(max_length=100 ,default='SOME STRING')
    position = models.CharField(max_length=2, choices=Position.choices, default=Position.CLERK)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'ID'

    objects = LibraryAdminManager()
    
    def get_position(self):
        return self.position

    def leave(self):
        self.left = True
        self.date_left =  date.today()
    
    def deactivate(self):
        self.is_active = False

    def activate(self):
        self.is_active = True
    
    def position_updating(self , pos):
        self.position = pos

    
   
