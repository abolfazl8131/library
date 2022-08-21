from pickle import TRUE
from django.db import models

# Create your models here.
class BookGenre(models.Model):
    genre = models.CharField(max_length = 100 , null = False , db_index = True , unique=True)
    

class BookClass(models.Model):
    name = models.CharField(max_length = 100 , null = False , db_index = True)
    genre = models.ForeignKey(BookGenre , on_delete = models.PROTECT)
    authors = models.TextField(null = True)
    slug = models.SlugField()
    quantity = models.IntegerField()


class BookObject(models.Model):
    code = models.CharField(max_length = 100 , null = False , db_index = True)
    date_published = models.DateField()
    published_no = models.SmallIntegerField()
    book_class = models.ForeignKey(BookClass , on_delete = models.CASCADE)
    