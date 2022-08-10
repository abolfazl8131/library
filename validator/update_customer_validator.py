from customer.models import Customer
import re
import datetime



class UpdateCustomerValidator:
    def __init__(self, data):

       
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.phone_number = data['phone_number']
        self.email = data["email"]
        self.birth_date = data['birth_date']

    def is_valid(self):
        statements = {
                      "first_name": self.first_name.isalpha() or None,
                      "last_name": self.last_name.isalpha() or None,
                      "phone_number": self.phone_number.isdigit() or None,
                    }
        flag = True
        list_of_errors = []

        # validate birthdate
        try:
            datetime.datetime.strptime(self.birth_date, '%Y-%m-%d')
        except ValueError:
            flag = False
            list_of_errors.append("Incorrect data format, should be YYYY-MM-DD")

        # validate email address
        EMAIL_REGEX = re.compile(r"[^@\s]+@[^@\s]+\.[a-zA-Z0-9]+$")

        if not EMAIL_REGEX.match(self.email):
            flag = False
            list_of_errors.append("enter a valid email address!")


        # validate firstname, lastname and phonenumber!
        if statements['first_name'] == False:
            list_of_errors.append("first name must be alpha!")
            flag = False

        if statements['last_name'] == False:
            list_of_errors.append("last name must be alpha!")
            flag = False

        if statements['phone_number'] == False:
            list_of_errors.append("please enter a valid phone number")
            flag = False

        if flag == False:
            return list_of_errors

        return True
