import random
from connect import ConnectionManager
from generator.person_generator import PersonGenerator


def insert_instructor(n):
    print("Inserting instructors...")
    
    instructor_column_names = connector.get_column_names("instructor")[1:-1]
    instructor_rating_column_names = connector.get_column_names("instructor_rating")
    universities_list = connector.get_columns(["university_id"], "university")
    for i in range(n):
        print(str(i+1)+"/"+str(n))
        person = generator.generate_person()
        university_id = random.choice(universities_list)[0]
        instructor_id = connector.insert(
            "instructor",
            instructor_column_names,
            (person["full_name"], person["email"], person["phone"], person["gender"], 0, 0, university_id,),
            return_id="instructor_id",
            add_creation_date=True
        )
        connector.insert(
            "instructor_rating",
            instructor_rating_column_names,
            (instructor_id, 0,)
        )
        connector.execute("CALL increment_university(%s)" % university_id)


def insert_assistant(n):
    print("Inserting assistants...")
    assistant_column_names = connector.get_column_names("assistant")[1:-1]
    for i in range(n):
        print(str(i+1) + "/" + str(n))
        person = generator.generate_person()
        connector.insert(
            "assistant",
            assistant_column_names,
            (person["full_name"], person["email"], person["phone"], person["gender"], 0,),
            add_creation_date=True
        )


def insert_student(n):
    print("Inserting students...")
    student_column_names = connector.get_column_names("student")[1:-1]
    for i in range(n):
        print(str(i+1)+"/"+str(n))
        person = generator.generate_person()
        connector.insert(
            "student",
            student_column_names,
            (person["full_name"], person["email"], person["phone"], person["birth_date"], person["age"], person["gender"], 0,),
            add_creation_date=True
        )


if __name__ == '__main__':
    connector = ConnectionManager()
    generator = PersonGenerator()
    insert_instructor(50)
    insert_assistant(10)
    insert_student(200)
    connector.close()
