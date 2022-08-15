from django.db import models
from django.db.models.query import QuerySet

class AdvancedDataQuery:
    def __init__(self , model:models.Model) -> None:
        self.model = model

    def query(self , **kwargs) -> QuerySet:
       
        for k, v in kwargs.items():
            if v != "":
                kwargs.pop(k)
            pass
        
        qs = self.model.objects.filter(kwargs)

        return qs

    