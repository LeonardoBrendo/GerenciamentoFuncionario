from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql+psycopg2://usuario:senha@localhost/carrosdb', echo=True)

Base = declarative_base()

class Carro(Base):
    __tablename__ = 'carros'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False)
    valor = Column(Float, nullable=False)
    ano = Column(Integer, nullable=False)

    def __repr__(self):
        return f"<Carro(nome='{self.nome}', valor={self.valor}, ano={self.ano})>"

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

class CarroModel:
    def adicionar_carro(self, carro):
        session.add(carro)
        session.commit()

    def listar_carros(self):
        return session.query(Carro).all()
