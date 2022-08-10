from customer.models import Customer
import re
import datetime




class IDCodeValidator:
    def __init__(self, data):
        self.ID = data['ID']

    def is_valid(self):
        try:
            if Customer.objects.get(ID=self.ID):
                return True
        except:

            return ["the customer with this ID code doesnt exist in database,,\
                if you have registered in the system, it maybe happend for poor connection!"]
