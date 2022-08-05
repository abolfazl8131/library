import datetime
from .models import SignInCode
from celery import shared_task
from django.utils import timezone
from pytz import UTC

@shared_task
def delete_otp():
    
        
    SignInCode.objects.filter(expirationTime__lte = timezone.now()).delete()
    print("deleteddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd")
       
    
