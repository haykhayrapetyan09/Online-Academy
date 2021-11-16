from connect import ConnectionManager
from faker import Faker
fake = Faker()

categories = {
    "Development":{
        "Web Development":["JavaScript", "React"],
        "Data Science":["Python", "Machine Learning", "Deep Learning"],
        "Programming Languages":["Java", "C#", "C++"]
    },
    "Business":{
        "Communication":["Technical Writing"],
        "Management":["Leaderhip","Management Skills"],
        "Sales":["Sales Skills"]
    },
    "Marketing":{
        "Digital Marketing":["Social Media Marketing","Internet Marketing"],
        "Branding":["Business Branding","Personal Branding"],
        "Product Marketing":["Marketing Plan"]
    }
}
universities = [line.strip() for line in open('recourses/universities.txt')]

def insert_categories(categories):
    print("Inserting categories, subcategories and topics...")
    for category in categories:
        connector.insert(
            "category",
            connector.get_column_names("category")[1:],
            (category, len(categories[category]),)
        )
        for subcategory in categories[category]:
            connector.insert(
                "subcategory",
                connector.get_column_names("subcategory")[1:],
                (subcategory, len(categories[category][subcategory]),connector.get_id("category_id","category", ["name",category]),)
            )
            for topic in categories[category][subcategory]:
                connector.insert(
                    "topic",
                    connector.get_column_names("topic")[1:],
                    (topic, 0, connector.get_id("subcategory_id", "subcategory", ["name", subcategory]),)
                )

def insert_universities(universities):
    print("Inserting universities...")
    for university in universities:
        connector.insert("university",
                         connector.get_column_names("university")[1:],
                         (university, fake.address(),0)
                        )


if __name__ == '__main__':
    connector = ConnectionManager()
    insert_universities(universities)
    insert_categories(categories)
    connector.close()


