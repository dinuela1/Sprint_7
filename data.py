from faker import Faker
import random

fake = Faker(locale='Ru_ru')

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
