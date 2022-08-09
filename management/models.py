from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
import enum
from django.utils.translation import gettext_lazy as _
# Create your models here.



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

    def get_position(self) -> Position :
        return self.Position[self.admin_position]
   
