import pandas as pd
import random
from connect import ConnectionManager
from faker import Faker
from datetime import time
from randomtimestamp import random_time
fake = Faker()


def insert_course(n):
    topics_list = connector.get_columns(["topic_id"], "topic")
    instructors_list = connector.get_columns(["instructor_id"], "instructor")
    assistants_list = connector.get_columns(["assistant_id"], "assistant")

    data = pd.read_csv("../recourses/udemy_courses.csv", usecols=["course_title", "price", "published_timestamp", "num_lectures"])
    length = len(data)
    if length < n:
        print("Given number (%d) is greater than dataset length (%d). Inserting %d courses" % (n, length, length))
        n = length

    courses = data.sample(n=n)
    courses = courses.rename(columns={"course_title": "title", "published_timestamp": "release_date", "num_lectures": "total_chapters"})

    courses["description"] = courses.apply(lambda _: fake.sentence(nb_words=10), axis=1)
    courses["language"] = courses.apply(lambda _: random.choice(["Armenian", "English", "French", "Spanish", "German", "Russian", "Chinese"]), axis=1)
    courses["release_date"] = courses["release_date"].str[:-10]

    courses = courses[["title", "description", "price", "language", "release_date", "total_chapters"]]
    courses["total_students"] = 0
    courses["topic_id"] = courses.apply(lambda _: random.choice(topics_list)[0], axis=1)
    courses["instructor_id"] = courses.apply(lambda _: random.choice(instructors_list)[0], axis=1)
    courses["assistant_id"] = courses.apply(lambda _: random.choice(assistants_list)[0], axis=1)
    courses = list(courses.itertuples(index=False))

    print("Inserting courses with exams and chapters...")
    i = 1
    course_column_names = connector.get_column_names("course")[1:]
    course_rating_column_names = connector.get_column_names("course_rating")
    exam_column_names = connector.get_column_names("exam")[1:]
    chapter_column_names = connector.get_column_names("chapter")[1:]

    for course in courses:
        print(str(i)+"/"+str(n))
        i += 1
        course_id = connector.insert(
            "course",
            course_column_names,
            course,
            "course_id"
        )
        connector.insert(
            "course_rating",
            course_rating_column_names,
            (course_id, 0,)
        )
        connector.execute("CALL increment_instructor(%s)" % course.instructor_id)
        connector.execute("CALL increment_assistant(%s)" % course.assistant_id)
        connector.execute("CALL increment_topic(%s)" % course.topic_id)
        insert_exam(exam_column_names, course_id, course.title)
        insert_chapters(chapter_column_names, course_id, course.title, course.total_chapters)


def insert_chapters(chapter_column_names, course_id, course_title, n):
    chapters = [("Chapter "+str(i)+" in course: "+course_title, course_id) for i in range(1, n+1)]
    connector.insert_list(
        "chapter",
        chapter_column_names,
        chapters
    )


def insert_exam(exam_column_names, course_id, course_title):
    title = "Exam: "+course_title
    total_questions = random.randrange(10, 50, 5)
    max_time = random_time(start=time(0, 10), end=time(3, 0)).replace(second=0, microsecond=0)
    connector.insert(
        "exam",
        exam_column_names,
        (title, total_questions, max_time, course_id,)
    )


if __name__ == '__main__':
    connector = ConnectionManager()
    insert_course(100)
    connector.close()
