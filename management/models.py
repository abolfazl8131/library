
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from datetime import date
# Create your models here.
    

class Position(models.TextChoices):
    MASTER = 'MS', _('Master')
    CASHIER = 'CA', _('Cashier')
    CLERK = 'CL', _('Clerk')
        


class LibraryAdmin(User):
  
    ID = models.CharField(max_length=100, unique=True, db_index=True , default='SOME STRING')
    birth_date = models.DateField(null=True)
    date_left = models.DateField(null=True)
    left = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=100 ,default='SOME STRING')
    position = models.CharField(max_length=2, choices=Position.choices, default=Position.CLERK)
    company = ''
    
    
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

    
   
