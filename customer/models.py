
from django.contrib.auth.base_user import AbstractBaseUser

from django.db import models


class Customer(AbstractBaseUser):
    ID = models.CharField(max_length=100, unique=True, db_index=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birth_date = models.DateField(null=True)
    date_joined = models.DateField(null=True)
    date_left = models.DateField(null=True)
    left = models.BooleanField(default=False)
    email = models.EmailField()
    phone_number = models.CharField(max_length=100)

    USERNAME_FIELD = 'ID'


class SignInCode(models.Model):
    code = models.CharField(unique=True, max_length=100, db_index=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    expirationTime = models.DateTimeField()




