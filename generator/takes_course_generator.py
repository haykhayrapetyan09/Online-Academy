import datetime
from connect import ConnectionManager
from randomtimestamp import randomtimestamp


def generate_takes_course(n):
    print("Generating takes courses...")
    takes_course_column_names = connector.get_column_names("takes_course")
    join = " JOIN chapter ch ON pc.course_id = ch.course_id " \
           "LEFT JOIN takes_course tc ON pc.student_id = tc.student_id and ch.chapter_id = tc.chapter_id " \
           "WHERE tc.chapter_id IS NULL " \
           "ORDER BY random() " \
           "LIMIT %d" % n

    available_takes_course_list = connector.get_columns(
        ["pc.student_id", "ch.chapter_id", "pc.date"],
        "purchases_course pc",
        condition=join
    )

    length = len(available_takes_course_list)
    if length == 0:
        print("There is no available takes courses. Please insert new purchases.")
        return 0
    elif length < n:
        print("Available takes courses are less than given number (%d). Inserting %d takes courses" % (n, length))

    i = 1
    for takes_course in available_takes_course_list:
        print(str(i) + "/" + str(length))
        i += 1
        student_id = takes_course[0]
        chapter_id = takes_course[1]
        date = takes_course[2]

        date = datetime.datetime(date.year, date.month, date.day)
        start_date = randomtimestamp(start=date)
        end_date = randomtimestamp(start=start_date)

        connector.insert(
            "takes_course",
            takes_course_column_names,
            (student_id, chapter_id, start_date, end_date,)
        )


if __name__ == '__main__':
    connector = ConnectionManager()
    generate_takes_course(500)
    connector.close()
