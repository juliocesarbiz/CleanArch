import pytest
from sqlalchemy import text
from src.infra.db.settings.connection import DBConnectionHandler
from src.infra.db.repositories.users_repository import UserRepository


db_connection_handler = DBConnectionHandler()
connection = db_connection_handler.get_engine().connect()

@pytest.mark.skip(reason='Sensive test')
def test_insert_user():
    mocked_first_name = 'first'
    mocked_last_name = 'last'
    mocked_age = 30

    user_repo = UserRepository()
    user_repo.insert_user(mocked_first_name, mocked_last_name, mocked_age)


    sql = '''
        select * from clean_database.users
        where first_name = '{}'
        AND last_name = '{}'
        AND age = {}
    '''.format(mocked_first_name, mocked_last_name, mocked_age)

    response = connection.execute(text(sql))
    registry = response.fetchall()[0]

    assert registry.first_name == mocked_first_name
    assert registry.last_name == mocked_last_name
    assert registry.age == mocked_age

    connection.execute(text(f'''
    DELETE FROM clean_database.users where id = {registry.id}
    '''))

    connection.commit()

def test_select_user():
    mocked_first_name = 'first2'
    mocked_last_name = 'last2'
    mocked_age = 100

    sql =  '''
        INSERT INTO clean_database.users (FIRST_NAME, LAST_NAME, AGE) VALUES ('{}', '{}', {})
    '''.format(mocked_first_name, mocked_last_name, mocked_age)

    connection.execute(sql)
    #connection.commit()

    user_repository = UserRepository()
    response = user_repository.select_user(mocked_first_name)
    print("Test Select")
    print(response)