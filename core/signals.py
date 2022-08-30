import time
import datetime
from django.db.models.signals import pre_save, post_save, pre_delete , post_delete
from .models import LoanBook , Loan , Basket
from django.dispatch import receiver

@receiver(pre_save , sender = LoanBook)
def create_loanbook(sender,  instance, **kwargs):
    book_object = instance.book_object
    book_object.unavailable()
    book_object.save()


@receiver(post_delete , sender = Basket)
def delete_basket(sender,  instance, **kwargs):
    book_object = instance.book_object
    book_object.available = True
    book_object.save()

@receiver(post_save , sender = Basket)
def create_basket(sender, instance , **kwargs):
    book_object = instance.book_object
    book_object.available = False
    book_object.save()