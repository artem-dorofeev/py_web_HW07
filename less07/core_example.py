from sqlalchemy import create_engine, Table, Column, Integer, String, ForeignKey, MetaData
from sqlalchemy.sql import select


engine = create_engine('sqlite:///:memory:', echo=False)
metadata = MetaData()

users = Table('users', metadata,
              Column('id', Integer, primary_key=True),
              #   Column('name', String),
              Column('fullname', String),
              )

addresses = Table('addresses', metadata,
                  Column('id', Integer, primary_key=True),
                  Column('email_address', String(100), nullable=False),
                  Column('user_id', Integer, ForeignKey('users.id')),
                  )

metadata.create_all(engine)

if __name__ == '__main__':
    with engine.connect() as conn:
        r_user = users.insert().values(fullname='Artem Dorofeev')
        print(r_user)
        result_user = conn.execute(r_user)
        print(result_user.lastrowid)

        u = conn.execute(select(users))
        ok = 'OK'
        print(u.all(), ok)

        r_adress = addresses.insert().values(
            email_address="artem@i.ua", user_id=result_user.lastrowid)
        conn.execute(r_adress)

        a = conn.execute(select(addresses))
        print(a.all(), ok)

        a_u = select(users.c.fullname, addresses.c.email_address).select_from(
            addresses).join(users)

        a_u = select(users.c.fullname, addresses.c.email_address).join(users)
        result = conn.execute(a_u)
        print(result.fetchall())
