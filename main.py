import sqlalchemy
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column, Integer, String

def setup_database():
    engine = sqlalchemy.create_engine('sqlite:///5sbdorm.db')
    Base = declarative_base()
    Base.metadata.create_all(engine)
    return engine, Base

engine, Base = setup_database()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    age = Column(Integer)
    username = Column(String(50))
    password = Column(String(50))

    def __repr__(self):
        return f"<User(name={self.name}, age={self.age}, username={self.username})>"

Base.metadata.create_all(engine)

# Criação de usuários com entrada do usuário
num_users = int(input("Quantos usuários você deseja adicionar? "))
for _ in range(num_users):
    name = input("Digite o nome do usuário: ")
    age = int(input("Digite a idade do usuário: "))
    username = input("Digite o nome de usuário: ")
    password = input("Digite a senha: ")

    new_user = User(name=name, age=age, username=username, password=password)

    Session = sessionmaker(bind=engine)
    session = Session()

    session.add(new_user)
    session.commit()

# Consulta e exibição de usuários
print("Usuários cadastrados:")
for instance in session.query(User).order_by(User.id):
    print(instance.name, instance.age, instance.username)
