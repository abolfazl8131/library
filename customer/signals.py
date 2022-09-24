
import datetime
from django.db.models.signals import pre_save
from django.dispatch import receiver


from customer.models import Customer, SignInCode
from datetime import date

@receiver(pre_save , sender = Customer)
def create_customer(sender,  instance, **kwargs):
    if not instance.date_joined:
        instance.date_joined = date.today()


def update_customer(sender, **kwargs):
    pass


def delete_customer(sender, **kwargs):
    pass

@receiver(pre_save , sender = SignInCode)
def create_code(sender,instance, **kwargs):
    instance.expirationTime = datetime.datetime.now() + datetime.timedelta(minutes=3)
