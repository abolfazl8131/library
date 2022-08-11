import time
import datetime
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.http import JsonResponse

from .models import *
from datetime import date

@receiver(pre_save , sender = LibraryAdmin)
def create_customer(sender,  instance, **kwargs):
    instance.admin_date_joined = date.today()

