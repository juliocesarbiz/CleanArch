from src.infra.db.tests.user_repository import UserRepositorySpy
from src.data.use_cases.user_register import UserRegister

def test_register():
    first_name = 'firstname'
    last_name = 'lastname'
    age = 22

    repo = UserRepositorySpy()
    user_register = UserRegister(repo)

    response = user_register.register(first_name, last_name, age)
    
    assert repo.insert_user_attributes['first_name'] == first_name
    assert response['type'] == 'Users'
    assert response['count'] == 1
    assert response['attributes'] 
