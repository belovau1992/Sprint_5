import random
from faker import Faker

faker = Faker('ru_RU')

def generate_registration_data():
    name = faker.first_name()
    random_numbers = str(random.randint(0, 999)).zfill(3)
    email = f"andreibelov21_{random_numbers}@{faker.free_email_domain()}"
    password = faker.password(length=6, special_chars=True, digits=True, upper_case=True, lower_case=True)
    return name,email, password