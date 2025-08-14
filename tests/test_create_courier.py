import pytest
import requests
import allure
from url import *
from data import *

fake = Faker()


@allure.title('Проверяем работу ручки создания курьера /api/v1/courier с методом POST')
class TestCreateCourier:

    @allure.title('Создаем нового курьера и проверяем код статуса')
    def test_create_new_courier_success(self, generate_courier_data):
        response = requests.post(f'{main_link}{api_create}', data=generate_courier_data)
        assert response.status_code == 201 and (response.text == courier_creation_success)


    @allure.title('Создаем двух одинаковых курьеров')
    def test_create_two_similar_courier_failure(self, create_courier_and_delete):
        response = requests.post(f'{main_link}{api_create}', data=create_courier_and_delete)
        assert response.status_code == 409 and (response.text == courier_creation_failure_409)

    @allure.title('Создание курьера с отсутствующими данными')
    @pytest.mark.parametrize('data_setup', registration)
    def test_create_courier_without_data(self, data_setup):
        response = requests.post(f'{main_link}{api_create}', data=data_setup)
        assert response.status_code == 400 and (response.text == not_enough_data)
