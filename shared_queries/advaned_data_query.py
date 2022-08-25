
from django.db import models
from django.db.models.query import QuerySet
import threading

class AdvancedDataQuery(threading.Thread):
    def __init__(self , model:models.Model) -> None:
        threading.Thread.__init__(self)
        self.model = model

    def data_query(self , **kwargs) -> QuerySet:
       
        for k, v in list(kwargs.items()):
            if v == "":
               kwargs.pop(k)
            else:
                pass 
        
        qs = self.model.objects.filter(**kwargs)
       
        
        return qs

    