from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Criação da base declarativa
Base = declarative_base()

# Definindo a tabela 'Pessoa'
class Pessoa(Base):
    __tablename__ = 'pessoa'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False)
    idade = Column(Integer, nullable=False)
    altura = Column(Float, nullable=False)
    profissao = Column(String, nullable=False)

# Conectando ao banco de dados PostgreSQL
DATABASE_URL = "postgresql+psycopg2://x:y@localhost/senac"
engine = create_engine(DATABASE_URL)

# Criando as tabelas no banco de dados
Base.metadata.create_all(engine)

# Criando a sessão
Session = sessionmaker(bind=engine)
session = Session()

# Exemplo de inserção de um novo registro na tabela pessoa
nova_pessoa = Pessoa(nome="João", idade=30, altura=1.75, profissao="Engenheiro")
session.add(nova_pessoa)
session.commit()

# Consulta simples
pessoas = session.query(Pessoa).all()
for pessoa in pessoas:
    print(f"Nome: {pessoa.nome}, Idade: {pessoa.idade}, Altura: {pessoa.altura}, Profissão: {pessoa.profissao}")
