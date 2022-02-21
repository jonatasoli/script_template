import pytest
from src.main import get_data_futstats

fake_api = dict(category='test')

def test_response_is_list():
    """Must return list"""
    response = get_data_futstats()
    assert isinstance(response, list)


def test_response_is_fake_list(mocker):
    """Must return fake dict"""
    mocker.patch(
        "src.main.get_data_futstats",
        return_value=fake_api
    )
    response = get_data_futstats()
    assert response == [dict(category='test')]
