from sqlalchemy import Column, create_engine, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
engine = create_engine('sqlite:///database.db')
Session = sessionmaker(bind=engine)


class Pessoa(Base):
    __tablename__ = 'pessoa'
    id = Column(Integer, primary_key=True)
    nome = Column(String(200), nullable=False)

    def __repr__(self):
        return "ID: %d, nome: %s" % (self.id, self.nome)


class Endereco(Base):
    __tablename__ = 'endereco'
    id = Column(Integer, primary_key=True)
    nm_rua = Column(String(100))
    bairro = Column(String(100))
    cep = Column(String(20))
    id_pessoa = Column(Integer, ForeignKey('pessoa.id'))
    pessoa = relationship(Pessoa)



class Cadastro:
    def __init__(self):
        self.pessoa = None
        self.endereco = None
        self.session = Session()

    def cadastrar_pessoa(self, id, nome):
        self.pessoa = Pessoa(id=id, nome=nome)
        return self.pessoa

    def cadastrar_endereco(self, **kwargs):
        self.endereco = Endereco(**kwargs)
        return self.endereco

    def salvar(self):
        if self.pessoa and self.endereco:
            self.session.add(self.pessoa)
            self.session.add(self.endereco)
            self.session.commit()

    def get_pessoa_by_name(self, name):
        query = self.session.query(Pessoa).filter(Pessoa.nome.like('%{}%'.format(name))).order_by(Pessoa.id)
        return query.all()



if __name__ == "__main__":
    Base.metadata.create_all(engine)
    cadastro = Cadastro()
    #p = cadastro.cadastrar_pessoa(id=18778765, nome='David Gilmour')
    #endereco = {'id': 2, 'nm_rua': 'Rua das amelias', 'bairro': 'Cruzeiro', 'cep': '37876000', 'id_pessoa': p.id, 'pessoa': p }
    #cadastro.cadastrar_endereco(**endereco)
    #cadastro.salvar()
    for p in cadastro.get_pessoa_by_name(name='David'):
        print(p)
