from contextlib import ContextDecorator
from lib2to3.pytree import Base
from unicodedata import name
from faker import Faker
fake = Faker()

class BaseContact:
    def __init__(self, firstname, surname, phone, email):
        self.firstname = firstname
        self.surname = surname
        self.phone = phone
        self.email = email

    def contact(self):
        return f"Wybieram numer {self.phone} i dzwonię do {self.firstname} {self.surname}"


    def __str__(self):
        return f'{self.firstname} {self.surname}, {self.email}'
        
    @property
    def label_lenght(self):
        return len(self.firstname + '' + self.surname)

class BusinessContact(BaseContact):
    def __init__(self, company, position, business_phone, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.company = company
        self.position = position
        self.business_phone = business_phone

    def contact(self):
        return f"Wybieram numer biznesowy {self.business_phone} i dzwonię do {self.firstname} {self.surname}"

def generate_fake_persons():
    persons = []
    fake = Faker()
    for _ in range(5):
        persons.append(BaseContact(firstname = fake.first_name(), surname = fake.last_name(), phone = fake.phone_number(), email = fake.email()))
    return persons

def generate_fake_persons_business():
    persons_business = []
    fake = Faker()
    for _ in range(5):
        persons_business.append(BusinessContact(firstname = fake.first_name(), surname = fake.last_name(),phone = fake.phone_number(), email = fake.email(), company = fake.company(), position = fake.job(), business_phone = fake.phone_number()))
    return persons_business

namelist = generate_fake_persons()
namelist_business = generate_fake_persons_business()

for name in namelist:
    print(name)
    print(name.contact())
    print(f'Dugość imienia i nazwiska to {name.label_lenght}')
    print('-------------------------------')

for name_business in namelist_business:
    print(name_business)
    print(name_business.contact())
    print(f'Dugość imienia i nazwiska to {name_business.label_lenght}')
    print('-------------------------------')

def create_contacts(type, amount):
    base_card = []
    business_card = []
    fake = Faker()
    if type == BaseContact:
        for i in range(amount):
            base_card.append(BaseContact(firstname = fake.first_name(), surname = fake.last_name(), phone = fake.phone_number(), email = fake.email()))
            return base_card

    if type == BusinessContact:
        for i in range(amount):
            business_card.append(BusinessContact(firstname = fake.first_name(), surname = fake.last_name(),phone = fake.phone_number(), email = fake.email(), company = fake.company(), position = fake.job(), business_phone = fake.phone_number()))
            return business_card
















