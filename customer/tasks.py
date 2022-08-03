import datetime
from .models import SignInCode
from celery import shared_task

@shared_task
def delete_otp():
    try:
        sign_code = SignInCode.objects.get(expirationTime = datetime.datetime.now())
        sign_code.delete()
    except:
        pass