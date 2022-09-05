import time
import datetime
from django.db.models.signals import pre_save, post_save, pre_delete , post_delete
from .models import LoanBook , LoanModel , Basket
from django.dispatch import receiver
import uuid


@receiver(post_delete , sender = Basket)
def delete_basket(sender,  instance, **kwargs):
    book_object = instance.book_object
    book_object.is_available()
    book_object.save()

@receiver(post_save , sender = Basket)
def create_basket(sender, instance , **kwargs):
    book_object = instance.book_object
    book_object.unavailable()
    book_object.save()


@receiver(pre_save , sender = LoanModel)
def create_loan_object(sender,  instance, **kwargs):
    
    instance.date_submitted = datetime.datetime.now()
