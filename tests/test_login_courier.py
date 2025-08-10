import requests
import allure
from url import *
from generate_courier import register_new_courier_and_return_login_password
from faker import Faker

fake = Faker()


@allure.title('Проверяем работу ручки авторизации курьера /api/v1/courier/login с методом POST')
class TestLoginCourier:

    @allure.title('Авторизация существующего курьера и проверка кода статуса')
    def test_login_courier_code_200(self):
        data = register_new_courier_and_return_login_password()
        login = data[0]
        password = data[1]
        response = requests.post(f'{main_link}{api_login}', data={
            'login': login, 'password': password
        })
        assert response.status_code == 200
        r = response.json()
        courier_id = r['id']
        requests.delete(f'{main_link}{api_delete}{courier_id}')

    @allure.title('Авторизация существующего курьера и проверка получение id')
    def test_login_courier_get_id(self):
        data = register_new_courier_and_return_login_password()
        login = data[0]
        password = data[1]
        response = requests.post(f'{main_link}{api_login}', data={
            'login': login, 'password': password
        })
        r = response.json()
        assert r['id']
        r = response.json()
        courier_id = r['id']
        requests.delete(f'{main_link}{api_delete}{courier_id}')

    @allure.title('Авторизация существующего курьера с неверным паролем')
    def test_login_courier_with_wrong_password_404(self):
        data = register_new_courier_and_return_login_password()
        login = data[0]
        password = data[1] + '123'
        response = requests.post(f'{main_link}{api_login}', data={
            'login': login, 'password': password
        })
        assert response.status_code == 404
        password = data[1]
        response_correct = requests.post(f'{main_link}{api_login}', data={
            'login': login, 'password': password
        })
        r = response_correct.json()
        courier_id = r['id']
        requests.delete(f'{main_link}{api_delete}{courier_id}')

    @allure.title('Авторизация существующего курьера с неверным логином')
    def test_login_courier_with_wrong_login_404(self):
        data = register_new_courier_and_return_login_password()
        login = data[0] + '123'
        password = data[1]
        response = requests.post(f'{main_link}{api_login}', data={
            'login': login, 'password': password
        })
        assert response.status_code == 404
        login = data[0]
        response_correct = requests.post(f'{main_link}{api_login}', data={
            'login': login, 'password': password
        })
        r = response_correct.json()
        courier_id = r['id']
        requests.delete(f'{main_link}{api_delete}{courier_id}')

    @allure.title('Авторизация существующего курьера без логина')
    def test_login_courier_without_login_400(self):
        data = register_new_courier_and_return_login_password()
        response = requests.post(f'{main_link}{api_login}', data={
            'password': data[1]
        })
        assert response.status_code == 400
        response = requests.post(f'{main_link}{api_login}', data={
            'login': data[0], 'password': data[1]
        })
        r = response.json()
        courier_id = r['id']
        requests.delete(f'{main_link}{api_delete}{courier_id}')

    @allure.title('Авторизация существующего курьера без пароля')
    def test_login_courier_without_password_400(self):
        data = register_new_courier_and_return_login_password()
        response = requests.post(f'{main_link}{api_login}', data={
            'login': data[0]
        })
        assert response.status_code == 400
        response = requests.post(f'{main_link}{api_login}', data={
            'login': data[0], 'password': data[1]
        })
        r = response.json()
        courier_id = r['id']
        requests.delete(f'{main_link}{api_delete}{courier_id}')

    @allure.title('Авторизация несуществующего курьера')
    def test_login_courier_without_password_404(self):
        login = fake.name()
        password = fake.password()
        response = requests.post(f'{main_link}{api_login}', data={
            'login': login, 'password': password
        })
        assert response.status_code == 404

