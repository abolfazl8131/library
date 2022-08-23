
from django.db import models
from django.db.models.query import QuerySet

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
        print(qs)
        
        return qs

    