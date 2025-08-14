import requests
import allure
from url import *
from data import *

fake = Faker()


@allure.title('Проверяем работу ручки авторизации курьера /api/v1/courier/login с методом POST')
class TestLoginCourier:

    @allure.title('Авторизация существующего курьера')
    def test_login_courier_code_200(self, create_courier_and_delete):
        response = requests.post(f'{main_link}{api_login}', data=create_courier_and_delete)
        assert response.status_code == 200 and (response.json()['id'])


    @allure.title('Авторизация существующего курьера без логина')
    def test_login_courier_without_login_400(self, create_courier_and_delete):
        changed_data = {'login': '', 'password': create_courier_and_delete[3]}
        response = requests.post(f'{main_link}{api_login}', data=changed_data)
        assert response.status_code == 400 and (response.json() == not_enough_data_to_login)

    @allure.title('Авторизация существующего курьера без пароля')
    def test_login_courier_without_password_400(self, create_courier_and_delete):
        data_no_password = {'login': create_courier_and_delete[2], 'password': ''}
        response = requests.post(f'{main_link}{api_login}', data=data_no_password)
        assert response.status_code == 400 and (response.json() == not_enough_data_to_login)

    @allure.title('Авторизация несуществующего курьера')
    def test_login_not_existing_courier_404(self, fake_data):
        response = requests.post(f'{main_link}{api_login}', data=fake_data)
        assert response.status_code == 404 and (response.json() == courier_not_found)

