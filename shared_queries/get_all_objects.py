from django.db import models
from django.http import Http404
import threading
from company.models import Company

class GetManagementObjects:
    
    def __init__(self , model:models.Model,company:Company):
       
        self.model = model
        self.company = company

    def get_all(self,  **kwargs):
        for k, v in list(kwargs.items()):
            
            kwargs[k] = self.company
           
        list_of_obj = self.model.objects.filter(**kwargs , company = self.company)
        return list_of_obj

    def get_object(self , **kwargs):
        try:
           
            obj = self.model.objects.get(**kwargs , company = self.company)
            
            return obj
        
        except Exception as e: 
            print(e)
            raise Http404
    
    def run(self):
        
        t1 = threading.Thread(target=self.get_all)
        t2 = threading.Thread(target=self.get_object)
        t1.start()
        t2.start()
        t1.join()
        t2.join()


   

   