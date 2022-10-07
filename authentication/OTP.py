import random
import string
from customer.tasks import sms , email
from customer.models import SignInCode, Customer
import base64

class OTP:
    def __init__(self, data , sending_type):
        self.type = sending_type
        self.ID = data["ID"]

    def choose(self):

        if self.type == 1:
            return self.sms()

        elif self.type == 2:
            return self.email()

  
    def sms(self):
        return sms(self)

    def email(self):
        return email(self)

    def create(self):

        encoded_otp = base64.b64encode(bytes(self.generate_code(), 'utf-8'))
        

        obj =  SignInCode.objects.create(customer= self.get_customer() ,  code = encoded_otp)
                                 

        return base64.b64decode(obj.code).decode()


    def generate_code(self):

        characters = list(string.ascii_letters + string.digits)

        random.shuffle(characters)

        password = []
        
        for _ in range(8):

            password.append(random.choice(characters))

        random.shuffle(password)

        return ("".join(password))
    

    def get_customer(self):

        customer = Customer.objects.get(ID=self.ID)

        return customer


