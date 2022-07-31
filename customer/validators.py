
class SignUpValidator:
    def __init__(self, data):

        self.ID = data['ID']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.phone_number = data['phone_number']

    def is_valid(self):
        statements = { "ID" : self.ID.isdigit(),
                        "first_name" : self.first_name.isalpha(),
                        "last_name" : self.last_name.isalpha(),
                        "phone_number" : self.phone_number.isdigit(),
                        }
        flag = True
        list_of_errors = []

        if statements['ID'] == False:
            list_of_errors.append("ID is not digit! please enter a valid data")
            flag = False

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