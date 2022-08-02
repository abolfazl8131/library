import random
import string

from customer.models import SignInCode, Customer


class OTP:
    def __init__(self, data , sending_type):
        self.type = sending_type
        self.ID = data["ID"]

    def choose(self):

        if self.type == 1:
            self.sms()

        elif self.type == 2:
            self.email()

    def sms(self):
        otp_code = self.create()
        return otp_code

    def email(self):
        otp_code = self.create()
        return otp_code

    def create(self):
        object =  SignInCode.objects.create(customer= self.get_customer() ,
                                  code = self.generate_code())
        return object.code


    def generate_code(self):

        characters = list(string.ascii_letters + string.digits)
        random.shuffle(characters)

        password = []
        for i in range(8):
            password.append(random.choice(characters))

        random.shuffle(password)

        return ("".join(password))

    def get_customer(self):
        customer = Customer.objects.get(ID=self.ID)
        return customer


