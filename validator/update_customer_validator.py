from customer.models import Customer
import re
import datetime
from validator.validators import AbstractFieldsValidator


class UpdateCustomerValidator(AbstractFieldsValidator):
    def __init__(self, data):
        self.position = None

    