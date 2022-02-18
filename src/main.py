import httpx
from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from loguru import logger

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



def get_data_futstats():
    _headers = {"accept": "application/json", "Authorization": "Bearer 583cda5b-7ba"}
    _urls = "http://apifutebol.footstats.com.br/3.1/championships"
    return httpx.get(_urls, headers=_headers).json()['data']


def save_data(obj):
    with session as s:
        s.bulk_save_objects(obj)
        s.commit()


def create_batch_data(domain_object):
    data_object = []
    for i in domain_object:
        data_object.append(Championship(
            active=i['active'], category=i['category'], collectType=i['collectType'], collectTypePt=i['collectTypePt'],
            country=i['country'], cupName=i['cupName'], currentPhase=i['currentPhase'], currentRound=i['currentRound'],
            hasClassification=i['hasClassification'], hasGroupClassification=i['hasGroupClassification'], id=i['id'],
            idCurrentPhase=i['idCurrentPhase'], name=i['name'], numberRounds=i['numberRounds']
        ))
    return data_object


def capture_data(capture_function):
    return capture_function()


def process_service():
    domain_object = capture_data(get_data_futstats)
    data_object = create_batch_data(domain_object)
    save_data(data_object)
    logger.info('Process Finished')


if __name__ == '__main__':
    process_service()
