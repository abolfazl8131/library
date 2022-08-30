from pickle import TRUE
import unittest
from django.db import models

# Create your models here.
class BookGenre(models.Model):
    genre = models.CharField(max_length = 100 , null = False , db_index = True , unique=True)
    

class BookClass(models.Model):
    name = models.CharField(max_length = 100 , null = False , db_index = True , unique= True)
    genre = models.ForeignKey(BookGenre , on_delete = models.PROTECT)
    authors = models.TextField(null = True)
    quantity = models.IntegerField(default=0)

    def increase_quantity(self):
        self.quantity += 1
    
    def decrease_quantity(self):
        self.quantity -= 1


class BookObject(models.Model):
    
    code = models.CharField(max_length = 100 , null = False , db_index = True , unique= True)
    date_published = models.DateField()
    published_no = models.SmallIntegerField()
    book_class = models.ForeignKey(BookClass , on_delete = models.PROTECT)
    available = models.BooleanField(default=True)

    def unavailable(self):
        self.available = False

    def is_available(self):
        self.available = True








    

    