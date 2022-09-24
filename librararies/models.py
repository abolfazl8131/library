from django.db import models

# Create your models here.

class Company(models.Model):
    name = models.CharField(unique = False , db_index=True , max_length=100)
    city = models.CharField(max_length=100)
    county = models.CharField(max_length=100)
    province = models.CharField(max_length=100)
    phone_num = models.CharField()
    