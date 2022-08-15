from django.db import models
from django.http import Http404

class GetObjectsByParams:
    def __init__(self , model:models.Model):
        self.model = model

    def get_object(self , **kwargs):
        try:
           
            obj = self.model.objects.get(**kwargs)
            return obj
        
        except: 
            
            return Http404

   