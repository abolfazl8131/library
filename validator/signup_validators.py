
from validator.validators import AbstractUserFieldsValidator

# this class does all validation of signup informations
class SignUpValidator(AbstractUserFieldsValidator):
    
    def __init__(self, data):

        try:
            self.position = data['position']
        except:
            self.position = None


    