import json
from connect import ConnectionManager
from faker import Faker
fake = Faker()


with open("../resources/categories.txt") as file:
    categories = json.load(file)
with open('../resources/universities.txt') as file:
    universities = [line.strip() for line in file]


def insert_categories(categories):
    print("Inserting categories, subcategories and topics...")
    category_column_names = connector.get_column_names("category")[1:-1]
    subcategory_column_names = connector.get_column_names("subcategory")[1:-1]
    topic_column_names = connector.get_column_names("topic")[1:-1]
    n = len(categories)
    i = 1
    for category in categories:
        print(str(i) + "/" + str(n))
        i += 1
        category_id = connector.insert(
            "category",
            category_column_names,
            (category, len(categories[category]),),
            return_id="category_id",
            add_creation_date=True
        )
        for subcategory in categories[category]:
            subcategory_id = connector.insert(
                "subcategory",
                subcategory_column_names,
                (subcategory, len(categories[category][subcategory]), category_id,),
                return_id="subcategory_id",
                add_creation_date=True
            )
            for topic in categories[category][subcategory]:
                connector.insert(
                    "topic",
                    topic_column_names,
                    (topic, 0, subcategory_id,),
                    add_creation_date=True
                )


def insert_universities(universities):
    print("Inserting universities...")
    n = len(universities)
    i = 1
    university_column_names = connector.get_column_names("university")[1:-1]
    for university in universities:
        print(str(i)+"/"+str(n))
        i += 1
        connector.insert(
            "university",
            university_column_names,
            (university, fake.address(), 0),
            add_creation_date=True
        )


if __name__ == '__main__':
    connector = ConnectionManager()
    insert_universities(universities)
    insert_categories(categories)
    connector.close()
