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
    q = BookObject.objects.filter(book_class__name = class_.name).count()
    class_.quantity = q
    class_.save() 
    


@receiver(pre_delete , sender = BookObject)
def delete_book(sender,  instance, **kwargs):
    class_ = instance.book_class
    class_.decrease_quantity()
    class_.save() 
    