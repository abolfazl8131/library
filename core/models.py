
from django.db import models
from customer.models import *
from book.models import *
import uuid
# Create your models here.

class LoanModel(models.Model):
    id = models.UUIDField(primary_key = True,default = uuid.uuid4,editable = False)
    borrower = models.ForeignKey(Customer , on_delete=models.CASCADE) 
    date_submitted = models.DateTimeField(null = True)

class LoanBook(models.Model):
    loan = models.ForeignKey(LoanModel , on_delete=models.CASCADE)
    book_object = models.ForeignKey(BookObject , on_delete=models.PROTECT)

class Basket(models.Model):
    customer = models.ForeignKey(Customer , on_delete=models.CASCADE)
    book_object = models.ForeignKey(BookObject , on_delete=models.PROTECT)
    date_submitted = models.DateField(null= True)