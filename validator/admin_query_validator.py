
from validator.validators import AbstractUserQueryInterface

class AdminQueryValidator(AbstractUserQueryInterface):
    def __init__(self, data: dict) -> None:
        self.data = data