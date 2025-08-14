import requests
import allure
from url import *
from data import *
import pytest


@allure.title('Проверяем работу ручки создания заказа /api/v1/orders с методом POST')
class TestCreateOrder:

    @allure.title('Создание заказа с валидными данными и разными вариантами цветов')
    @pytest.mark.parametrize("color_value", scooter_color)
    def test_create_order_with_color_code_201(self, color_value):
        order_data = payload
        order_data['color'] = color_value
        response = requests.post(f'{main_link}{api_order}', data=order_data)
        assert response.status_code == 201 and (track_message in response.text)
        requests.put(f'{main_link}{api_order_cancel}', data={'track': response.json()['track']})
