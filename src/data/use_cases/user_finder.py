#pylint: disable=broad-exception-raised

from typing import Dict
from src.domain.use_cases.user_finder import UserFinder as UserFinderInterface
from src.data.interfaces.users_repository import UserRepositoryInterface

class UserFinder(UserFinderInterface):
    def __init__(self, users_repository: UserRepositoryInterface) -> None:
        self.__users_repository = users_repository

    def find(self, first_name: str) -> Dict:
        if not first_name.isalpha():
            raise Exception('Nome invalido para a busca')
        
        if len(first_name) > 18:
            raise Exception('Nome muito grande para a busca')
        
        users = self.__users_repository.select_user(first_name)

        if users == []:
            raise Exception('Usuario nao encontrado')
        
        response = {
                'type':'Users',
                'count':len(users),
                'attributes':users,
        }

        return response
 

