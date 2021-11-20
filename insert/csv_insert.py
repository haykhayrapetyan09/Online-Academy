import pandas as pd
import random
from connect import ConnectionManager
from faker import Faker
fake = Faker()

def insert_course(n, topics_list, instructors_list, assistants_list):
    data = pd.read_csv("../recourses/udemy_courses.csv", usecols=["course_title", "price", "published_timestamp", "num_lectures"])
    courses = data.sample(n=n)
    courses = courses.rename(columns={"course_title": "title", "published_timestamp": "release_date", "num_lectures":"total_chapters"})

    courses["description"] = courses.apply(lambda _: fake.sentence(nb_words=10), axis=1)
    courses["language"] = courses.apply(lambda _: random.choice(["Armenian", "English", "French", "Spanish", "German", "Russian", "Chinese"]), axis=1)
    courses["release_date"] = courses["release_date"].str[:-10]

    courses = courses[["title", "description", "price", "language", "release_date","total_chapters"]]
    courses["total_students"] = 0
    courses["price"] = courses["price"].astype(int)
    courses["total_students"] = courses["total_students"].astype(int)
    courses["topic_id"] = courses.apply(lambda _: random.choice(topics_list)[0], axis=1).astype(int)
    courses["instructor_id"] = courses.apply(lambda _: random.choice(instructors_list)[0], axis=1).astype(int)
    courses["assistant_id"] = courses.apply(lambda _: random.choice(assistants_list)[0], axis=1).astype(int)

    courses = list(courses.to_records(index=False))
    i=1
    for course in courses:
        print(str(i)+"/"+str(n))
        i+=1
        print(course)
        course_id = connector.insert(
            "course",
            connector.get_column_names("course")[1:],
            course
        )
        print("courseid =",course_id)
        connector.insert(
            "course_rating",
            connector.get_column_names("course_rating"),
            (course_id, 0,)
        )

if __name__ == '__main__':
    connector = ConnectionManager()
    topics_list = connector.get_ids("topic_id", "topic")
    instructors_list = connector.get_ids("instructor_id", "instructor")
    assistants_list = connector.get_ids("assistant_id", "assistant")
    insert_course(50, topics_list, instructors_list, assistants_list)
    print(connector.get_column_names("course")[1:])
    connector.close()
