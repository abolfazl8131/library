from customer.models import Customer
import re
import datetime


# this class does all validation of signup informations
class SignUpValidator:
    
    def __init__(self, data):

        self.ID = data['ID']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.phone_number = data['phone_number']
        self.email = data["email"]
        self.birth_date = data['birth_date']

    def is_valid(self):
        statements = {"ID": self.ID.isdigit(),
                      "first_name": self.first_name.isalpha(),
                      "last_name": self.last_name.isalpha(),
                      "phone_number": self.phone_number.isdigit(),
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

        # ID validator, if ID is not digit
        if statements['ID'] == False:
            list_of_errors.append("ID is not digit! please enter a valid data")
            flag = False

        # check ID is in DB or not!
        try:
            if self.model.objects.get(ID=self.ID):
                flag = False
                list_of_errors.append("your ID code must be unique in system!")

        except:
            pass

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
