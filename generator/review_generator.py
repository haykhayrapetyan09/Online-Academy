import random
from faker import Faker
from connect import ConnectionManager
from randomtimestamp import randomtimestamp
fake = Faker()


def generate_review(n):
    print("Generating reviews...")
    review_column_names = connector.get_column_names("review")
    join = "JOIN exam e ON te.exam_id = e.exam_id " \
           "JOIN course cs ON e.course_id = cs.course_id " \
           "LEFT JOIN review r ON te.student_id = r.student_id " \
           "AND cs.course_id = r.course_id AND cs.instructor_id = r.instructor_id " \
           "WHERE r.student_id IS NULL " \
           "ORDER BY random() " \
           "LIMIT %d" % n

    available_review_list = connector.get_columns(
        ["te.student_id", "cs.course_id", "cs.instructor_id", "te.end_time"],
        "takes_exam te",
        condition=join
    )

    length = len(available_review_list)
    if length == 0:
        print("There is no available reviews. Please insert new takes exams.")
        return 0
    elif length < n:
        print("Available reviews are less than given number (%d). Inserting %d reviews" % (n, length))

    i = 1
    for review in available_review_list:
        print(str(i) + "/" + str(length))
        i += 1
        student_id = review[0]
        course_id = review[1]
        instructor_id = review[2]
        end_time = review[3]

        date = randomtimestamp(start=end_time)
        course_rating = random.randint(0, 5)
        instructor_rating = random.randint(0, 5)
        feedback = fake.sentence(nb_words=20)

        connector.insert(
            "review",
            review_column_names,
            (student_id, course_id, instructor_id, course_rating, instructor_rating, feedback, date,)
        )


if __name__ == '__main__':
    connector = ConnectionManager()
    generate_review(10)
    connector.close()
