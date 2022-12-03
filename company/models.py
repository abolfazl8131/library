from django.db import models

# Create your models here.

class Company(models.Model):
    
    name = models.CharField(unique = False , db_index=True , max_length=100)
    city = models.CharField(max_length=100 , db_index = True)
    county = models.CharField(max_length=100, db_index = True)
    province = models.CharField(max_length=100, db_index = True)
    phone_num = models.CharField(max_length = 100)
    address = models.TextField()
    is_active = models.BooleanField(default=False)

    