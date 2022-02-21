import httpx
from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from loguru import logger
from decouple import config

from src.models import Championship


def get_session():
    engine = create_engine('sqlite:///teste.db')
    Session = sessionmaker(bind=engine)
    return Session()


def get_data_futstats():
    _headers = {"accept": "application/json", "Authorization": config("TOKEN")}
    _urls = "http://apifutebol.footstats.com.br/3.1/championships"
    return httpx.get(_urls, headers=_headers).json()['data']


def save_data(obj):
    with get_session() as s:
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
    logger.info('Process Start')
    domain_object = capture_data(get_data_futstats)
    data_object = create_batch_data(domain_object)
    save_data(data_object)
    logger.info('Process Finished')


if __name__ == '__main__':
    process_service()
