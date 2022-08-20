from customer.models import Customer
import re
import datetime
from validator.validators import AbstractUserFieldsValidator


class UpdateCustomerValidator(AbstractUserFieldsValidator):
    def __init__(self, data):
        self.position = None

    