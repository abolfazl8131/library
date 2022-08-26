import time
import datetime
from django.db.models.signals import pre_save, post_save, pre_delete
from .models import LoanBook , Loan
from django.dispatch import receiver

@receiver(pre_save , LoanBook)

def create_loanbook(sender,  instance, **kwargs):
    book_object = instance.book_object
    book_object.available = False
    book_object.save()