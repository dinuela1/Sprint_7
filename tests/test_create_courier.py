import requests
import allure
from url import *
from generate_courier import register_new_courier_and_return_login_password
from faker import Faker

fake = Faker()

@allure.title('Проверяем работу ручки создания курьера /api/v1/courier с методом POST')
class TestCreateCourier:

    @allure.title('Создаем нового курьера и проверяем код статуса')
    def test_create_new_courier_code_201(self):
        login = fake.name()
        password = fake.password()
        firstName = fake.first_name()
        response = requests.post(f'{main_link}{api_create}', data={
            'login': login, 'password': password, 'firstName': firstName
        })
        assert response.status_code == 201
        courier_login = requests.post(f'{main_link}{api_login}', data={
            'login': login, 'password': password
        })
        c = courier_login.json()
        courier_id = c['id']
        requests.delete(f'{main_link}{api_delete}{courier_id}')


    @allure.title('Создаем нового курьера и проверяем текст ответа')
    def test_create_new_courier_text_ok_true(self):
        login = fake.name()
        password = fake.password()
        firstName = fake.first_name()
        response = requests.post(f'{main_link}{api_create}', data={
            'login': login, 'password': password, 'firstName': firstName
        })
        assert response.text == '{"ok":true}'


    @allure.title('Создаем двух одинаковых курьеров')
    def test_create_two_similar_courier_409(self):
        new_data = register_new_courier_and_return_login_password()
        new_data_api = {
            "login": new_data[0],
            "password": new_data[1]
        }
        response = requests.post(f'{main_link}{api_create}', data=new_data_api)
        assert response.status_code == 409
        courier_login = requests.post(f'{main_link}{api_login}', data=new_data_api)
        c = courier_login.json()
        courier_id = c['id']
        requests.delete(f'{main_link}{api_delete}{courier_id}')

    @allure.title('Создание курьера с паролем без указания логина')
    def test_create_courier_without_login_400(self):
        password = fake.password()
        response = requests.post(f'{main_link}{api_create}', data={
            'password': password
        })
        assert response.status_code == 400

    @allure.title('Создание курьера с логином без указания пароля')
    def test_create_courier_without_password_400(self):
        login = fake.name()
        response = requests.post(f'{main_link}{api_create}', data={
            'login': login
        })
        assert response.status_code == 400


    @allure.title('Создание курьера с существующим логином')
    def test_create_courier_with_existing_login(self):
        login = fake.name()
        password = fake.password()
        password_2 = fake.password()
        requests.post(f'{main_link}{api_create}', data={
            'login': login, 'password': password
        })
        response = requests.post(f'{main_link}{api_create}', data={
            'login': login, 'password': password_2
        })
        assert response.status_code == 409
