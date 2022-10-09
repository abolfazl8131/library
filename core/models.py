
from django.db import models
from customer.models import Customer
from book.models import BookObject
import uuid
# Create your models here.

class LoanModel(models.Model):

    id = models.UUIDField(primary_key = True,default = uuid.uuid4,editable = False)
    borrower = models.ForeignKey(Customer , on_delete=models.CASCADE , related_name = 'renter') 
    date_submitted = models.DateTimeField(null = True)
    delivered = models.BooleanField(default=False)
    end_rent = models.BooleanField(default=False)
    

    def is_delivered(self):
        self.delivered = True

    def end(self):
        self.end_rent = True


class LoanBook(models.Model):
    loan = models.ForeignKey(LoanModel , on_delete=models.CASCADE , related_name='loan_model')
    book_object = models.ForeignKey(BookObject , on_delete=models.PROTECT , related_name = 'book_obj')
    

class Basket(models.Model):
    customer = models.ForeignKey(Customer , on_delete=models.CASCADE)
    book_object = models.ForeignKey(BookObject , on_delete=models.PROTECT)
    date_submitted = models.DateField(null= True)

