import datetime
import random
from connect import ConnectionManager
from randomtimestamp import randomtimestamp


def generate_takes_course(n):
    print("Generating takes courses...")
    # takes_course_column_names = connector.get_column_names("takes_course")
    # join = "JOIN chapter ON purchases_course.course_id = chapter.course_id"
    # purchases_chapters_list = connector.get_columns(["student_id", "chapter_id"], "purchases_course", condition=join)
    for i in range(n):
        print(str(i + 1) + "/" + str(n))
        i += 1
        # student_id, chapter_id, date = random.choice(purchases_chapters_list)


if __name__ == '__main__':
    connector = ConnectionManager()
    generate_takes_course(100)
    connector.close()
