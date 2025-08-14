from faker import Faker
import random

fake = Faker(locale='Ru_ru')

scooter_color = [['BLACK'], ['GREY'], (['BLACK'], ['GREY']), ['']]

color = []
num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
payload = {
    "firstName" : fake.first_name(),
    "lastName" : fake.last_name(),
    "address" : fake.address(),
    "metroStation" : random.choice(num),
    "phone" : fake.phone_number(),
    "rentTime" : random.choice(num),
    "deliveryDate" : fake.date('2025-08-11'),
    "comment" : fake.text(15),
    "color" : color
}

fake_1 = Faker()

login = fake_1.name()
password = fake_1.password()
firstName = fake_1.first_name()

data_to_create = {
    'login': login,
    'password': password,
    'firstName': firstName
}

courier_creation_success = '{"ok":true}'
courier_creation_failure_409 = '{"message": "Этот логин уже используется"}'
not_enough_data = '{"code":400,"message":"Недостаточно данных для создания учетной записи"}'
not_enough_data_to_login = '{"code":400,"message":"Недостаточно данных для входа"}'
courier_not_found = '{"code":404,"message":"Учетная запись не найдена"}'
registration = [{'password': password, 'firstName': firstName}, {'login': login, 'firstName': firstName}]
track_message = 'track'
orders_message = 'orders'