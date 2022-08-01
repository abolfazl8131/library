from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.http import JsonResponse

from customer.models import Customer
from datetime import date
@receiver(pre_save , sender = Customer)
def create_customer(sender,  instance, **kwargs):
    instance.date_joined = date.today()


def update_customer(sender, **kwargs):
    pass


def delete_customer(sender, **kwargs):
    pass


def auto_delete_code(sender, **kwargs):
    pass


def create_code(sender, **kwargs):
    pass
