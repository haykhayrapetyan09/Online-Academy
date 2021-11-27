import datetime
import random
from connect import ConnectionManager
from randomtimestamp import randomtimestamp


def generate_views_course(n):
    print("Generating views...")
    views_course_column_names = connector.get_column_names("views_course")[1:]
    students_list = connector.get_columns(["student_id"], "student")
    courses_list = connector.get_columns(["course_id, release_date"], "course")
    for i in range(n):
        print(str(i + 1) + "/" + str(n))
        i += 1
        student_id = random.choice(students_list)[0]
        course_id, release_date = random.choice(courses_list)
        release_date = datetime.datetime(release_date.year, release_date.month, release_date.day)
        date = randomtimestamp(start=release_date)
        connector.insert(
            "views_course",
            views_course_column_names,
            (student_id, course_id, date,)
        )


if __name__ == '__main__':
    connector = ConnectionManager()
    generate_views_course(100)
    connector.close()
