
from .models import SignInCode
from celery import shared_task
from django.utils import timezone

from django.conf import settings


@shared_task
def delete_otp():
    
        
    SignInCode.objects.filter(expirationTime__lte = timezone.now()).delete()
    



@shared_task(queue=settings.CELERY_PRIO_QUEUE)    
def sms(self):
    otp_code = self.create()
    return otp_code

@shared_task(queue=settings.CELERY_PRIO_QUEUE) 
def email(self):
    otp_code = self.create()
    return otp_code

       
    

