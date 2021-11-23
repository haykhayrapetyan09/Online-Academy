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
    category_column_names = connector.get_column_names("category")[1:]
    subcategory_column_names = connector.get_column_names("subcategory")[1:]
    topic_column_names = connector.get_column_names("topic")[1:]
    n = len(categories)
    i = 1
    for category in categories:
        print(str(i) + "/" + str(n))
        i += 1
        category_id = connector.insert(
            "category",
            category_column_names,
            (category, len(categories[category]),),
            "category_id"
        )
        for subcategory in categories[category]:
            subcategory_id = connector.insert(
                "subcategory",
                subcategory_column_names,
                (subcategory, len(categories[category][subcategory]),category_id,),
                "subcategory_id"
            )
            for topic in categories[category][subcategory]:
                connector.insert(
                    "topic",
                    topic_column_names,
                    (topic, 0, subcategory_id,)
                )

def insert_universities(universities):
    print("Inserting universities...")
    n = len(universities)
    i=1
    university_column_names = connector.get_column_names("university")[1:]
    for university in universities:
        print(str(i)+"/"+str(n))
        i+=1
        connector.insert("university",
                         university_column_names,
                         (university, fake.address(),0)
                        )


if __name__ == '__main__':
    connector = ConnectionManager()
    insert_universities(universities)
    insert_categories(categories)
    connector.close()


