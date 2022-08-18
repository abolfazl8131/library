from django.db import models

class GetObjects:
    def __init__(self , model:models.Model):
        self.model = model

    def get_all(self):
        list_of_obj = self.model.objects.all()
        return list_of_obj

   