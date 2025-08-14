import requests
import allure
from url import *
from data import *


@allure.title('Проверяем работу ручки получения списка заказов /api/v1/orders с методом GET')
class TestGetListOfOrders:

    @allure.title('Получаем список всех имеющихся заказов')
    def test_get_list_of_orders(self):
        response = requests.get(f'{main_link}{api_order}')
        assert orders_message in response.text
