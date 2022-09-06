
from ast import Delete

from ..models import LoanModel
class LoanManager:
    def __init__(self) -> None:
        self.model = LoanModel

    def create(self , customer):
        try:
            loan_object = self.model.objects.create(borrower = customer)
            loan_object.save()
            return loan_object
        except Exception as e:
            raise e

    def update(self , status):
        pass

    def delete(self):
        pass

    def delivered(self , data):
        try:
            model = self.model.objects.get(id = data['id'])
            model.is_delivered()
            model.save()
            
        except Exception as e:
            raise e
    
    def end(self , data):
        try:
            
            loan_model = LoanModel.objects.get(id = data['id'])
            loan_model.end()
            loan_model.save()
            
        except Exception as e:
            raise e
        
        