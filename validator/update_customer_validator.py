
from validator.validators import AbstractUserFieldsValidator


class UpdateCustomerValidator(AbstractUserFieldsValidator):
    def __init__(self, data):
        self.ID = ""
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.phone_number = data['phone_number']
        self.email = data["email"]
        self.birth_date = data['birth_date']
        self.position = ""


    