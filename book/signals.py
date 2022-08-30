import time
import datetime
from django.db.models.signals import pre_save, post_save, pre_delete
from django.dispatch import receiver
from django.http import JsonResponse

from .models import *
from datetime import date


@receiver(pre_save , sender = BookObject)
def create_customer(sender,  instance, **kwargs):
    class_ = instance.book_class
    class_.increase_quantity()
    class_.save() 
    


@receiver(pre_delete , sender = BookObject)
def create_customer(sender,  instance, **kwargs):
    class_ = instance.book_class
    class_.decrease_quantity()
    class_.save() 
    