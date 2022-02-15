from faker import Faker
from datetime import date
from dateutil.relativedelta import *
fake = Faker()


class PersonGenerator:
    today = date.today()
    

    def generate_person(self):
        person = {}
        profile = fake.simple_profile()
        person["full_name"] = profile["name"]
        person["email"] = profile["mail"]
        person["phone"] = fake.phone_number()
        person["gender"] = profile["sex"]
        person["birth_date"] = profile["birthdate"]
        person["age"] = relativedelta(self.today, profile["birthdate"]).years
        return person
