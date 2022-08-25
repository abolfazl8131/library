from django.db import models
from django.http import Http404
import threading

class GetObjects(threading.Thread):
    
    def __init__(self , model:models.Model):
        threading.Thread.__init__(self)
        self.model = model

    def get_all(self):
        list_of_obj = self.model.objects.all()
        return list_of_obj

    def get_object(self , **kwargs):
        try:
           
            obj = self.model.objects.get(**kwargs)
            
            return obj
        
        except: 
            
            raise Http404

   

   