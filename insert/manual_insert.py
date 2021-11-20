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
universities = [line.strip() for line in open('../recourses/universities.txt')]

def insert_categories(categories):
    print("Inserting categories, subcategories and topics...")
    for category in categories:
        category_id = connector.insert(
            "category",
            connector.get_column_names("category")[1:],
            (category, len(categories[category]),),
            "category_id"
        )
        for subcategory in categories[category]:
            subcategory_id = connector.insert(
                "subcategory",
                connector.get_column_names("subcategory")[1:],
                (subcategory, len(categories[category][subcategory]),category_id,),
                "subcategory_id"
            )
            for topic in categories[category][subcategory]:
                connector.insert(
                    "topic",
                    connector.get_column_names("topic")[1:],
                    (topic, 0, subcategory_id,)
                )

def insert_universities(universities):
    print("Inserting universities...")
    n = len(universities)
    i=1
    for university in universities:
        print(str(i)+"/"+str(n))
        i+=1
        connector.insert("university",
                         connector.get_column_names("university")[1:],
                         (university, fake.address(),0)
                        )


if __name__ == '__main__':
    connector = ConnectionManager()
    insert_universities(universities)
    insert_categories(categories)
    connector.close()


