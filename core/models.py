from statistics import mode
from django.db import models
from customer.models import *
from book.models import *
# Create your models here.

class Loan(models.Model):
    slug = models.SlugField(unique=True , db_index=True , null= False)
    borrower = models.ForeignKey(Customer , on_delete=models.CASCADE) 

class LoanBook(models.Model):
    loan = models.ForeignKey(Loan , on_delete=models.CASCADE)
    book_object = models.ForeignKey(BookObject , on_delete=models.PROTECT)