from src.infra.db.tests.user_repository import UserRepositorySpy
from src.data.use_cases.user_finder import UserFinder
def test_find():
    first_name = 'meuNome'

    repo = UserRepositorySpy()
    user_finder = UserFinder(repo)

    response = user_finder.find(first_name)

    assert repo.select_user_attributes['first_name'] == first_name

    assert response['type'] == 'Users'
    assert response['count'] == len(response['attributes'])
    assert response['attributes']

def test_find_error_in_valid_name():
    first_name = 'meuNome123'

    repo = UserRepositorySpy()
    user_finder = UserFinder(repo)

    try:
        user_finder.find(first_name)
        assert False
    except Exception as expection:
        assert str(expection) == "Nome invalido para a busca"


def test_find_error_in_long_name():
    first_name = 'meuNomeewefewfewfwefewfewfewfewfewfewfwefewfewfw'

    repo = UserRepositorySpy()
    user_finder = UserFinder(repo)

    try:
        user_finder.find(first_name)
        assert False
    except Exception as expection:
        assert str(expection) == "Nome muito grande para a busca"


def test_find_error_user_not_found():
    class UsersRepositoryError(UserRepositorySpy):
        def select_user(self, first_name: str):
            return []
        
    first_name = 'meuNome'
    repo = UsersRepositoryError()
    user_finder = UserFinder(repo)

    try:
        user_finder.find(first_name)
        assert False
    except Exception as expection:
        assert str(expection) == "Usuario nao encontrado"