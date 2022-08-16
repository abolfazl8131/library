from customer.models import Customer
import re
import datetime
from validator.validators import AdminFieldsValidator


class UpdateCustomerValidator(AdminFieldsValidator):
    def __init__(self, data):
        self.position = None

    