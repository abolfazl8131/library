
from django.db import models
from django.db.models.query import QuerySet
import threading

class AdvancedDataQuery:
    def __init__(self , model:models.Model) -> None:
        
        self.model = model

    def data_query(self , **kwargs) -> QuerySet:
       
        for k, v in list(kwargs.items()):
            if v == "":
               kwargs.pop(k)
            else:
                pass 
        
        qs = self.model.objects.filter(**kwargs)
       
        
        return qs
    
    def run(self):
        
        t1 = threading.Thread(target=self.data_query)
        t1.start()
        t1.join()


    