from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///teste.db')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class Championship(Base):
    __tablename__ = 'championships'
    id = Column(Integer, primary_key=True, autoincrement=True)
    active = Column(Boolean())
    category = Column(String(250))
    collectType = Column(String(250))
    collectTypePt = Column(String(250))
    country = Column(String(250))
    cupName = Column(String(250))
    currentPhase = Column(String(250))
    currentRound = Column(Integer())
    hasClassification = Column(Boolean())
    hasGroupClassification = Column(Boolean())
    json_id = Column(Integer())
    idCurrentPhase = Column(Integer())
    name = Column(String(255))
    numberRounds = Column(Integer())


Base.metadata.create_all(engine)
