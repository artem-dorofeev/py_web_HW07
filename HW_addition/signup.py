from sqlalchemy.exc import SQLAlchemyError

from database.db import session
from database.models import User

if __name__ == '__main__':
    login = input('login: ')
    password = input('password: ')
    try:
        user = User(login=login, password=password)
        session.add(user)
        session.commit()
    except SQLAlchemyError as e:
        session.rollback()
        print(e)
    finally:
        session.close()
