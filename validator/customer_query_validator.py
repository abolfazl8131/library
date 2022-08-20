from .validators import *

class CustomerQueryValidator(AbstractUserQueryInterface):
    def __init__(self , data):
        self.data = data
        data['position'] = ""
        data['is_active'] = ""