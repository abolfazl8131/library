
import datetime
import re
from sys import flags

class AdminFieldsValidator:
    flag = True
    list_of_errors = []
    
    def __init__(self , data) -> None:

        self.ID = data['ID']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.phone_number = data['phone_number']
        self.email = data["email"]
        self.birth_date = data['birth_date']
        self.position = data['position']


        

    def is_valid(self):
        self.statements = {
                      "first_name": self.first_name.isalpha(),
                      "last_name": self.last_name.isalpha() ,
                      "phone_number": self.phone_number.isdigit(),
                      "ID":self.ID.isdigit()
                    }

        self.ID_validator()
        self.position_validator()
        self.birthdate_validator()
        self.email_validator()
        self.name_validator()
        self.phone_validator()

        if self.flag == False:
            return self.list_of_errors
        return True


    def ID_validator(self):
        if self.statements['ID'] == False:
            self.flag = False
            self.list_of_errors.append('please select valid ID code')

    def position_validator(self):
        if not self.position==None:
            if self.position not in ['MS' , 'CA' , 'CL']:
                self.flag = False
                self.list_of_errors.append("please choose a postion exists in ['MS' , 'CA' , 'CL']")
            pass
        pass

    def birthdate_validator(self):
        try:
            datetime.datetime.strptime(self.birth_date, '%Y-%m-%d')
        except ValueError:
            self.flag = False
            self.list_of_errors.append("Incorrect date format, should be YYYY-MM-DD")



    def email_validator(self):
        EMAIL_REGEX = re.compile(r"[^@\s]+@[^@\s]+\.[a-zA-Z0-9]+$")

        if not EMAIL_REGEX.match(self.email):
            self.flag = False
            self.list_of_errors.append("enter a valid email address!")



    def name_validator(self):
        if self.statements['first_name'] == False:
            self.list_of_errors.append("first name must be alpha!")
            self.flag = False

        if self.statements['last_name'] == False:
            self.list_of_errors.append("last name must be alpha!")
            self.flag = False

    


    def phone_validator(self):
        if self.statements['phone_number'] == False:
            self.list_of_errors.append("please enter a valid phone number")
            self.flag = False





class AdminQueryInterface:
    flag = True
    list_of_errors = []

    def __init__(self , data:dict) -> None:
        self.data = data

       
    def is_valid(self):
        self.admin_date_joined__gte_validator()
        self.admin_birth_date__in_validator()
        self.admin_date_joined__lte_validator()
        self.admin_date_left__gte_validator()
        self.admin_date_left__lte_validator()
        self.admin_is_active_validator()
        self.admin_position_validator()
        self.admin_left_validator()
        if self.flag == False:
            return self.list_of_errors
        return True

    def admin_date_joined__gte_validator(self):
        data = self.data['admin_date_joined__gte']
        if data != "":
            try:
                datetime.datetime.strptime(data, '%Y-%m-%d')
            except ValueError:
                self.flag = False
                self.list_of_errors.append("Incorrect date format, should be YYYY-MM-DD (admin date joined gte)")
        pass



    
    def admin_date_joined__lte_validator(self):
        data = self.data['admin_date_joined__lte']
        if data != "":
            try:
                datetime.datetime.strptime(data, '%Y-%m-%d')
            except ValueError:
                self.flag = False
                self.list_of_errors.append("Incorrect date format, should be YYYY-MM-DD (admin date joined lte)")
        pass

    def admin_left_validator(self):
        data = self.data['admin_left']
        if data != "":
            if isinstance(data , bool):
                self.flag = False
                self.list_of_errors.append("admin left is boolean (True or False)")
        pass

    def admin_is_active_validator(self):
        data = self.data['admin_is_active']
        if data != "":
            if isinstance(data , bool) == False:
                self.flag = False
                self.list_of_errors.append("is active is boolean data (True or False)")
        pass

    def admin_date_left__lte_validator(self):
        data = self.data['admin_date_left__lte']
        if data != "":
            try:
                datetime.datetime.strptime(data, '%Y-%m-%d')
            except ValueError:
                self.flag = False
                self.list_of_errors.append("Incorrect date format, should be YYYY-MM-DD (admin date left lte)")
        pass

    def admin_birth_date__in_validator(self):
        data = self.data['admin_birth_date__in']
        if data != "":
            try:
                datetime.datetime.strptime(data, '%Y-%m-%d')
            except ValueError:
                self.flag = False
                self.list_of_errors.append("Incorrect date format, should be YYYY-MM-DD (admin birth date)")
        pass

    def admin_date_left__gte_validator(self):
        data = self.data['admin_date_left__gte']

        if data != "":
            try:
                datetime.datetime.strptime(data, '%Y-%m-%d')
            except ValueError:
                self.flag = False
                self.list_of_errors.append("Incorrect date format, should be YYYY-MM-DD (admin date left gte)")
        pass

    def admin_position_validator(self):
        data = self.data['admin_position']

        if data != "":
            if data not in ['MS' , 'CL' , 'CA']:
                self.flag = False
                self.list_of_errors.append("please choose a position in [MS , CL , CA]")
        pass


    