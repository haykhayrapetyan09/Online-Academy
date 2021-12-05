import datetime
from connect import ConnectionManager
from randomtimestamp import randomtimestamp


def generate_purchases_course(n):
    print("Generating purchases...")
    purchases_course_column_names = connector.get_column_names("purchases_course")
    join = " CROSS JOIN course cs " \
           "LEFT JOIN purchases_course pc " \
           "ON st.student_id=pc.student_id and cs.course_id = pc.course_id " \
           "WHERE pc.student_id IS NULL " \
           "ORDER BY random() " \
           "LIMIT %d" % n

    available_purchases_list = connector.get_columns(
        ["st.student_id", "cs.course_id", "cs.price", "cs.release_date", "cs.instructor_id"],
        "student st",
        condition=join
    )

    length = len(available_purchases_list)
    if length == 0:
        print("There is no available purchases. Please insert new students or courses.")
        return 0
    elif length < n:
        print("Number of available purchases are less than given number. Inserting %d purchases" % length)

    i = 1
    for purchase in available_purchases_list:
        print(str(i) + "/" + str(length))
        i += 1
        student_id = purchase[0]
        course_id = purchase[1]
        price = purchase[2]
        release_date = purchase[3]
        instructor_id = purchase[4]

        release_date = datetime.datetime(release_date.year, release_date.month, release_date.day)
        date = randomtimestamp(start=release_date)

        connector.insert(
            "purchases_course",
            purchases_course_column_names,
            (student_id, course_id, date, price,)
        )

        connector.execute("CALL increment_student_purchased(%s)" % student_id)
        connector.execute("CALL increment_course_total_students(%s)" % course_id)
        connector.execute("CALL increment_instructor_total_students(%s)" % instructor_id)


if __name__ == '__main__':
    connector = ConnectionManager()
    generate_purchases_course(100)
    connector.close()
