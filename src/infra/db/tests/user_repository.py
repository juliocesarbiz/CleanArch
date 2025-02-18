from typing import List
from src.domain.models.users import Users

class UserRepositorySpy:

    def __init__(self) -> None:
        self.insert_user_attributes = {}
        self.select_user_attributes = {}

    def insert_user(self, first_name: str, last_name: str, age: int) -> None:
        self.insert_user_attributes['first_name'] = first_name
        self.insert_user_attributes['last_name'] = last_name
        self.insert_user_attributes['age'] = age

    def select_user(self, first_name: str) -> List[Users]:
        self.select_user_attributes['first_name'] = first_name
        return[
            Users(23, first_name, 'last_name', 43),
            Users(23, first_name, 'last_name2', 32)
        ]
