from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import scoped_session, sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///atividades.db', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

class Dinheiro(Base):
    __tablename__='dinheiro'

    id = Column(Integer, primary_key=True)
    dinheiro = Column(Integer)
    nome = Column(String(40), index=True)

    def __repr__(self):
        return '<Dinheiro {}>'.format(self.nome)

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()


class Rodada(Base):
    __tablename__='resultado'

    id = Column(Integer, primary_key=True)
    rodada = Column(Integer)
    primeiraMilhar = Column(Integer)
    segundaMilhar = Column(Integer)
    terceiraMilhar = Column(Integer)
    quartaMilhar = Column(Integer)
    quintaMilhar = Column(Integer)
    data = Column(String(18), index=True)





    def __repr__(self):
        return '<Rodada {}>'.format(self.rodada)

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()






class Evento(Base):
    __tablename__='evento'
    id = Column(Integer, primary_key=True)


    nome = Column(String(40), index=True)
    rodada = Column(Integer)
    milhar = Column(Integer)
    valor = Column(Integer)
    conferir = Column(Integer)

    def __repr__(self):
        return '<Evento {}>'.format(self.nome)

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()
class Usuarios(Base):
    __tablename__='usuarios'
    id = Column(Integer, primary_key=True)
    login = Column(String(20), unique=True)
    senha = Column(String(20))

    def __repr__(self):
        return '<Usuario {}>'.format(self.login)

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()

def init_db():
    Base.metadata.create_all(bind=engine)

if __name__ == '__main__':
    init_db()

