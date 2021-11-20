import random

from connect import ConnectionManager
from person_generator import PersonGenerator


def insert_instructor(n, universities_list):
    print("Inserting instructors...")
    for i in range(n):
        print(str(i+1)+"/"+str(n))
        i+=1
        person = generator.generate_person()
        university_id = random.choice(universities_list)[0]
        instructor_id = connector.insert(
            "instructor",
            connector.get_column_names("instructor")[1:],
            (person["full_name"],person["email"],person["phone"],person["gender"], 0, 0, university_id,),
            "instructor_id"
        )
        connector.insert(
            "instructor_rating",
            connector.get_column_names("instructor_rating"),
            (instructor_id,0,)
        )
        connector.execute("CALL increment_university(%s)" % university_id)

def insert_assistant(n):
    print("Inserting assistants...")
    for i in range(n):
        print(str(i+1) + "/" + str(n))
        i+=1
        person = generator.generate_person()
        connector.insert(
            "assistant",
            connector.get_column_names("assistant")[1:],
            (person["full_name"], person["email"], person["phone"], person["gender"], 0,)
        )

def insert_student(n):
    print("Inserting students...")
    for i in range(n):
        print(str(i+1)+"/"+str(n))
        i+=1
        person = generator.generate_person()
        connector.insert(
            "student",
            connector.get_column_names("student")[1:],
            (person["full_name"], person["email"], person["phone"], person["birth_date"], person["age"], person["gender"], 0,)
        )

if __name__ == '__main__':
    connector = ConnectionManager()
    generator = PersonGenerator()
    universities_list = connector.get_ids("university_id", "university")
    insert_instructor(30, universities_list)
    insert_assistant(10)
    insert_student(100)
    connector.close()
