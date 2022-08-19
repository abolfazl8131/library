from customer.models import Customer
import re
import datetime
from validator.validators import AbstractFieldsValidator

# this class does all validation of signup informations
class SignUpValidator(AbstractFieldsValidator):
    
    def __init__(self, data):

        try:
            self.position = data['position']
        except:
            self.position = None


    