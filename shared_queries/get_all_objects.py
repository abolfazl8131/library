from django.db import models
from django.http import Http404
import threading

class GetObjects:
    
    def __init__(self , model:models.Model):
       
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
    
    def run(self):
        
        t1 = threading.Thread(target=self.get_all)
        t2 = threading.Thread(target=self.get_object)
        t1.start()
        t2.start()
        t1.join()
        t2.join()


   

   