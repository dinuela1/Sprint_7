import pytest
import requests
from url import *
from faker import Faker
import json

fake = Faker()


@pytest.fixture
def create_courier_and_delete():
    login = fake.first_name()
    password = fake.password()
    name = fake.first_name()
    data_to_create = {
        'login': login, 'password': password, 'firstName': name
    }
    data_to_login = {
        'login': login, 'password': password
    }
    requests.post(f'{main_link}{api_create}', data=data_to_create)
    login_courier = requests.post(f'{main_link}{api_login}', data=data_to_login)
    yield [data_to_create, data_to_login, login, password]
    courier_id = login_courier.json()
    requests.delete(f'{main_link}{api_delete}{courier_id["id"]}')


@pytest.fixture
def generate_courier_data():
    login = fake.first_name()
    password = fake.password()
    name = fake.first_name()
    data_to_create = {
        'login': login, 'password': password, 'firstName': name
    }
    data_to_login = {
        'login': login, 'password': password
    }
    yield [data_to_create, data_to_login]
    login_courier = requests.post(f'{main_link}{api_login}', data=data_to_login)
    courier_id = login_courier.json()['id']
    requests.delete(f'{main_link}{api_delete}{courier_id}')
