from sqlalchemy import Column, Integer, String, ForeignKey, Date, DateTime, func, event
# from sqlalchemy.orm import relationship
from sqlalchemy.orm import declarative_base, relationship

# from database.db import engine
from db import engine

# from .db import Base

Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    login = Column(String(20), unique=True)
    password = Column(String(20))


class Todo(Base):
    __tablename__ = "todos"
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False, index=True)
    discription = Column(String(100), nullable=False, index=True)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now())
    user_id = Column('user_id', Integer, ForeignKey('users.id'))
    # це для sqlalchemy щоб розуміло щоб там є зв'язок
    user = relationship(User)


@event.listens_for(Todo, 'defore_update')
def update_updated_at(mapper, conn, target):
    target.updated_at = func.now()


Base.metadata.create_all(engine)


# class Teacher(Base):
#     __tablename__ = "teachers"
#     id = Column(Integer, primary_key=True)
#     fullname = Column(String(100), nullable=False)


# class Group(Base):
#     __tablename__ = "groups"
#     id = Column(Integer, primary_key=True)
#     name = Column(String(10), nullable=False)


# class Student(Base):
#     __tablename__ = "students"
#     id = Column(Integer, primary_key=True)
#     fullname = Column(String(100), nullable=False)
#     group_id = Column("group_id", ForeignKey("groups.id", ondelete="CASCADE"))
#     group = relationship("Group", backref="students")


# class Discipline(Base):
#     __tablename__ = "disciplines"
#     id = Column(Integer, primary_key=True)
#     name = Column(String(120), nullable=False)
#     teacher_id = Column("teacher_id", ForeignKey(
#         "teachers.id", ondelete="CASCADE"))
#     teacher = relationship("Teacher", backref="disciplines")


# class Grade(Base):
#     __tablename__ = "grades"
#     id = Column(Integer, primary_key=True)
#     grade = Column(Integer, nullable=False)
#     date_of = Column("date_of", Date, nullable=True)
#     student_id = Column("student_id", ForeignKey(
#         "students.id", ondelete="CASCADE"))
#     discipline_id = Column(
#         "discipline_id", ForeignKey("disciplines.id", ondelete="CASCADE")
#     )
#     student = relationship("Student", backref="grade")
#     discipline = relationship("Discipline", backref="grade")
