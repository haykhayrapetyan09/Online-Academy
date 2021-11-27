import datetime
import random
from connect import ConnectionManager
from randomtimestamp import randomtimestamp


def generate_purchases_course(n):
    print("Generating purchases...")
    purchases_course_column_names = connector.get_column_names("purchases_course")
    students_list = connector.get_columns(["student_id"], "student")
    courses_list = connector.get_columns(["course_id", "price", "release_date"], "course")
    for i in range(n):
        print(str(i + 1) + "/" + str(n))
        i += 1
        safe_insert_purchases_course(purchases_course_column_names, students_list, courses_list)


def safe_insert_purchases_course(purchases_course_column_names, students_list, courses_list):
    student_id = random.choice(students_list)[0]
    course_id, price, release_date = random.choice(courses_list)
    release_date = datetime.datetime(release_date.year, release_date.month, release_date.day)
    date = randomtimestamp(start=release_date)
    try:
        connector.insert(
            "purchases_course",
            purchases_course_column_names,
            (student_id, course_id, date, price,)
        )
    except:
        print("Rolling back")
        connector.execute("ROLLBACK")
        print("Trying once more with other input data...")
        safe_insert_purchases_course(purchases_course_column_names, students_list, courses_list)


if __name__ == '__main__':
    connector = ConnectionManager()
    generate_purchases_course(100)
    connector.close()
