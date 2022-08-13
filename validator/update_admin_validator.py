from management.models import LibraryAdmin
import re
import datetime



class UpdateAdminValidator:
    def __init__(self, data):

        self.ID = data['ID']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.phone_number = data['phone_number']
        self.email = data["email"]
        self.birth_date = data['birth_date']
        self.position = data['position']

    def is_valid(self):
        statements = {
                      "first_name": self.first_name.isalpha(),
                      "last_name": self.last_name.isalpha() ,
                      "phone_number": self.phone_number.isdigit(),
                      "ID":self.ID.isdigit()
                    }
        flag = True
        list_of_errors = []
        #validate ID

        if statements['ID'] == False:
            flag = False
            list_of_errors.append('please select valid ID code')
        

        #postiion validator for admin
        if not self.position==None:
            if self.position not in ['MS' , 'CA' , 'CL']:
                flag = False
                list_of_errors.append("please choose a postion exists in ['MS' , 'CA' , 'CL']")
            pass
        pass

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
