import time
import datetime
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.http import JsonResponse

from .models import *
from datetime import date


@receiver(pre_save , sender = BookObject)
def create_customer(sender,  instance, **kwargs):
    class_ = instance.book_class
    class_.quantity +=1
    class_.save() 
    