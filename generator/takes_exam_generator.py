import datetime
import random
from connect import ConnectionManager
from randomtimestamp import randomtimestamp


def generate_takes_exam(n):
    print("Generating takes exams...")
    takes_exam_column_names = connector.get_column_names("takes_exam")

    finishers = "(SELECT tc.student_id, ch.course_id, count(ch.course_id) total_chapters, e.exam_id, e.max_time " \
                "FROM takes_course tc " \
                "JOIN chapter ch ON tc.chapter_id = ch.chapter_id " \
                "JOIN exam e ON ch.course_id = e.course_id " \
                "GROUP BY tc.student_id, ch.course_id, e.exam_id)"

    join = " JOIN course cs ON f.course_id = cs.course_id AND f.total_chapters = cs.total_chapters " \
           "LEFT JOIN takes_exam te ON f.student_id = te.student_id AND f.exam_id = te.exam_id " \
           "WHERE te.exam_id IS NULL " \
           "ORDER BY random() " \
           "LIMIT %d" % n

    available_takes_exam_list = connector.get_columns(
        ["f.student_id", "f.exam_id", "f.max_time", "cs.release_date"],
        finishers + " f",
        condition=join
    )

    length = len(available_takes_exam_list)
    if length == 0:
        print("There is no available takes exams. Please insert new takes courses.")
        return 0
    elif length < n:
        print("Available takes exams are less than given number (%d). Inserting %d takes exams" % (n, length))

    i = 1
    for takes_exam in available_takes_exam_list:
        print(str(i) + "/" + str(length))
        i += 1
        student_id = takes_exam[0]
        exam_id = takes_exam[1]
        max_time = takes_exam[2]
        release_date = takes_exam[3]

        release_date = datetime.datetime(release_date.year, release_date.month, release_date.day)
        start_time = randomtimestamp(start=release_date)
        max_end_time = start_time + datetime.timedelta(hours=max_time.hour,
                                                       minutes=max_time.minute,
                                                       seconds=max_time.second)

        end_time = randomtimestamp(start=start_time, end=max_end_time)
        duration = end_time - start_time

        grade = random.randint(0, 100)

        connector.insert(
            "takes_exam",
            takes_exam_column_names,
            (student_id, exam_id, start_time, end_time, duration, grade,)
        )


if __name__ == '__main__':
    connector = ConnectionManager()
    generate_takes_exam(10)
    connector.close()
