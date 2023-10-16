from sqlalchemy import create_engine, Table, Column, Integer, String, ForeignKey, MetaData
from sqlalchemy.orm import relationship, declarative_base, sessionmaker


engine = create_engine('sqlite:///:memory:', echo=False)
DBSession = sessionmaker(bind=engine)
session = DBSession()

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    fullname = (String)


class Addresses(Base):
    __tablename__ = 'addresses'
    id = Column(Integer, primary_key=True)
    user_email = Column('email', String(100), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    # це для sqlalchemy щоб розуміло щоб там є зв'язок
    user = relationship(User)


Base.metadata.create_all(engine)

if __name__ == '__main__':
    new_user = User(fullname='Artem Dorofeev')
    session.add(new_user)

    new_adr = Addresses(user_email="artem@i.ua", user=new_user)
    session.add(new_adr)

    session.commit()

    # new_user2 = User(fullname='Diana Dorofeeva')
    # session.add(new_user2)

    # new_adr2 = Addresses(user_email="diana@i.ua", user=new_user2)
    # session.add(new_adr2)

    # session.commit()

    # u = session.query(User).one()
    # print(u.id, u.fullname)

    # a = session.query(Addresses).join(Addresses.user).all()
    # # print(a)
    # for _ in a:
    #     print(_.id, _.user_email, _.user.fullname)

    new_user2 = User(fullname='Diana Dorofeeva')
    session.add(new_user2)

    new_adr2 = Addresses(user_email="diana@i.ua", user=new_user2)
    session.add(new_adr2)

    b = session.query(Addresses).join(Addresses.user).all()
    # print(b)
    for _ in b:
        print(_.id, _.user_email, _.user.fullname)

    session.commit()

    session.close()
