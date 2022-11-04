
from django.db.models.signals import post_save, pre_delete , post_delete,pre_save
from django.dispatch import receiver
from datetime import date

from .models import BookObject,BookClass



@receiver(post_save , sender = BookObject)
def create_book(sender,  instance, **kwargs):
    class_ = instance.book_class
    class_.set_quantity()
    class_.save() 
    


@receiver(post_delete , sender = BookObject)
def delete_book(sender,  instance, **kwargs):
    class_ = instance.book_class
    class_.set_quantity()
    class_.save() 
    


@receiver(pre_save , sender = BookClass)
def save_book_class(sender,  instance, **kwargs):
    if instance.date_created == None:
        instance.date_created = date.today()
        instance.save()
    