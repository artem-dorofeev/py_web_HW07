from sqlalchemy import and_
from .db import session
from .models import User, Todo


def get_user(login) -> User:
    # user = session.query(User).filter(User.login == login).one()
    user = session.query(User).filter(User.login == login).first()
    return user


def create_todo(title, description, user):
    todo = Todo(title=title, description=description, user=user)
    session.add(todo)
    session.commit()
    session.close()


def get_all_todos(user) -> list[Todo]:
    todos = session.query(Todo).join(User).filter(
        Todo.user == user).all()  # filter == where
    return todos


def update_todo(_id, title, description, user) -> Todo:
    todo = session.query(Todo).filter(and_(Todo.user == user, Todo.id == _id))
    if todo:
        todo.update({'title': title, 'description': description})
        session.commit()
    session.close()
    return todo.first()
    # return todo.one()


def remove_todo(_id, user) -> int:
    r = session.query(Todo).filter(
        and_(Todo.user == user, Todo.id == _id)).delete()
    session.commit()
    session.close()
    return r
