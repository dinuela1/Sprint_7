import requests
import allure
from url import *
from data import *
import pytest

@allure.title('Проверяем работу ручки создания заказа /api/v1/orders с методом POST')
class TestCreateOrder:

    @allure.title('Создание заказа с валидными данными и разными вариантами цветов')
    @pytest.mark.parametrize("color_value", [["BLACK"], ["BLACK", "GREY"], []])
    def test_create_order_with_color_code_201(self, color_value):
        payload['color'] = color_value
        response = requests.post(f'{main_link}{api_order}', data=payload)
        assert response.status_code == 201
        r = response.json()
        cancel_track = r['track']
        requests.put(f'{main_link}{api_order_cancel}', data={
            'track': cancel_track
        })


    @allure.title('Создание заказа с валидными данными с черным цветом, проверка наличия track')
    def test_create_order_with_black_color_get_track(self):
        payload['color'] = ['BLACK']

        response = requests.post(f'{main_link}{api_order}', data=payload)
        assert 'track' in response.text
        r = response.json()
        cancel_track = r['track']
        requests.put(f'{main_link}{api_order_cancel}', data={
            'track': cancel_track
        })

    @allure.title('Создание заказа с валидными данными без указания цвета, проверка наличия track')
    def test_create_order_without_color_get_track(self):

        response = requests.post(f'{main_link}{api_order}', data=payload)
        assert 'track' in response.text
        r = response.json()
        cancel_track = r['track']
        requests.put(f'{main_link}{api_order_cancel}', data={
            'track': cancel_track
        })