
from django.db.models.signals import pre_save
from django.dispatch import receiver


from .models import LibraryAdmin
from datetime import date

@receiver(pre_save , sender = LibraryAdmin)
def create_admin(sender,  instance, **kwargs):
    instance.username = instance.ID
    if not instance.date_joined:

        instance.date_joined = date.today()
      

    if not instance.password:
        instance.is_useruser = None
        instance.set_password(instance.ID)
    
    


