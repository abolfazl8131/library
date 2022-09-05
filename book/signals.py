import time
import datetime
from django.db.models.signals import pre_save, post_save, pre_delete
from django.dispatch import receiver
from django.http import JsonResponse

from .models import *
from datetime import date


@receiver(post_save , sender = BookObject)
def create_book(sender,  instance, **kwargs):
    class_ = instance.book_class
    class_.set_quantity()
    class_.save() 
    


@receiver(pre_delete , sender = BookObject)
def delete_book(sender,  instance, **kwargs):
    class_ = instance.book_class
    class_.set_quantity()
    class_.save() 
    