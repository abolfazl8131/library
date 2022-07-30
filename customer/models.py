from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import User
from django.db import models

# Create your models here.



class Customer(AbstractBaseUser):
    ID = models.CharField(max_length=100 , unique= True, db_index=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birth_date = models.DateField(null=True)
    date_joined = models.DateField(null=True)
    date_left = models.DateField(null=True)
    def validate(self):
        pass
    def pre_create(self):
        pass
    def pre_update(self):
        pass
    def pre_delete(self):
        pass
