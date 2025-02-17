#from src.infra.db.settings.connection import DBConnectionHandler
from src.infra.db.repositories.users_repository import UserRepository

def test_insert_user():
    mocked_first_name = 'first'
    mocked_last_name = 'last'
    mocked_age = 30

    user_repo = UserRepository()
    user_repo.insert(mocked_first_name, mocked_last_name, mocked_age)
    