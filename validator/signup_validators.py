
from validator.validators import AbstractUserFieldsValidator

# this class does all validation of signup informations
class SignUpValidator(AbstractUserFieldsValidator):
    
    def __init__(self, data):

        try:
            self.position = data['position']
              
        except:
            self.position = None


        self.ID = data['ID']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.phone_number = data['phone_number']
        self.email = data["email"]
        self.birth_date = data['birth_date']