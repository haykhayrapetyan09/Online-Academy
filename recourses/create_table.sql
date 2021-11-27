DROP table IF EXISTS assistant;
DROP table IF EXISTS category;
DROP table IF EXISTS course;
DROP table IF EXISTS exam;
DROP table IF EXISTS chapter;
DROP table IF EXISTS instructor;
DROP table IF EXISTS purchases_course;
DROP table IF EXISTS review;
DROP table IF EXISTS student;
DROP table IF EXISTS subcategory;
DROP table IF EXISTS takes_course;
DROP table IF EXISTS takes_exam;
DROP table IF EXISTS topic;
DROP table IF EXISTS university;
DROP table IF EXISTS views_course;
DROP table IF EXISTS course_rating;
DROP table IF EXISTS instructor_rating;

CREATE TABLE assistant
(
 assistant_id  serial PRIMARY KEY NOT NULL,
 full_name     varchar(50) NOT NULL,
 email         varchar(50) NOT NULL,
 phone         varchar(50),
 gender        char(1),
 total_courses int DEFAULT 0
);



CREATE TABLE category
(
 category_id         serial PRIMARY KEY NOT NULL,
 name                varchar(100) NOT NULL,
 total_subcategories int DEFAULT 0
);


CREATE TABLE subcategory
(
 subcategory_id serial PRIMARY KEY NOT NULL,
 name           varchar(100) NOT NULL,
 total_topics   int DEFAULT 0,
 category_id    int NOT NULL
);
CREATE INDEX subcategory_category ON subcategory(category_id);



CREATE TABLE topic
(
 topic_id         serial PRIMARY KEY NOT NULL,
 name             varchar(100) NOT NULL,
 total_courses    int DEFAULT 0,
 subcategory_id   int NOT NULL
);
CREATE INDEX topic_subcategory ON topic(subcategory_id);


CREATE TABLE university
(
 university_id     serial PRIMARY KEY NOT NULL,
 name              text NOT NULL,
 address           text NOT NULL,
 total_instructors int DEFAULT 0
);


CREATE TABLE instructor
(
 instructor_id   serial PRIMARY KEY NOT NULL,
 full_name       varchar(50) NOT NULL,
 email           varchar(50) NOT NULL,
 phone           varchar(50),
 gender          char(1),
 total_students  int DEFAULT 0,
 total_courses   int DEFAULT 0,
 university_id   int
);
CREATE INDEX instructor_university ON instructor(university_id);

CREATE TABLE instructor_rating
(
 instructor_id int PRIMARY KEY NOT NULL,
 rating        decimal(2,1)
);
CREATE INDEX instructor_rating_instructor ON instructor_rating(instructor_id);


CREATE TABLE course
(
 course_id       serial PRIMARY KEY NOT NULL,
 title           text NOT NULL,
 description     text NOT NULL,
 price           decimal(6,2) NOT NULL,
 language        varchar(50) NOT NULL,
 release_date    date NOT NULL,
 total_chapters  int DEFAULT 0,
 total_students  int DEFAULT 0,
 topic_id        int NOT NULL,
 instructor_id   int NOT NULL,
 assistant_id    int NOT NULL
);
CREATE INDEX course_topic ON course(topic_id);
CREATE INDEX course_instructor ON course(instructor_id);
CREATE INDEX course_assistant ON course(assistant_id);


CREATE TABLE course_rating
(
 course_id     int PRIMARY KEY NOT NULL,
 rating        decimal(2,1)
);
CREATE INDEX course_rating_course ON course_rating(course_id);


CREATE TABLE review
(
 student_id        int NOT NULL,
 course_id         int NOT NULL,
 instructor_id     int NOT NULL,
 course_rating     decimal(2,1),
 instructor_rating decimal(2,1),
 feedback          text,
 "date"            timestamp,
 PRIMARY KEY ( student_id, course_id, instructor_id )
);
CREATE INDEX review_student ON review(student_id);
CREATE INDEX review_course ON review(course_id);
CREATE INDEX review_instructor ON review(instructor_id);


CREATE TABLE exam
(
 exam_id         serial PRIMARY KEY NOT NULL,
 title           text NOT NULL,
 total_questions smallint NOT NULL,
 max_time          time NOT NULL,
 course_id       int NOT NULL
);
CREATE INDEX exam_course ON exam(course_id);


CREATE TABLE student
(
 student_id        serial PRIMARY KEY NOT NULL,
 full_name         varchar(50) NOT NULL,
 email             varchar(50) NOT NULL,
 phone             varchar(50),
 birth_date        date NOT NULL,
 age               smallint NOT NULL,
 gender            char(1),
 purchased_courses smallint DEFAULT 0
);


CREATE TABLE takes_exam
(
 student_id int NOT NULL,
 exam_id    int NOT NULL,
 "date"     date NOT NULL,
 start_time time NOT NULL,
 end_time   time,
 duration   time,
 grade      smallint,
 PRIMARY KEY ( student_id, exam_id )
);
CREATE INDEX takes_exam_student ON takes_exam(student_id);
CREATE INDEX takes_exam_exam ON takes_exam(exam_id);



CREATE TABLE views_course
(
 view_id serial PRIMARY KEY NOT NULL,
 student_id int NOT NULL,
 course_id  int NOT NULL,
 "date"     timestamp NOT NULL
);
CREATE INDEX views_course_student ON views_course(student_id);
CREATE INDEX views_course_course ON views_course(course_id);



CREATE TABLE purchases_course
(
 student_id int NOT NULL,
 course_id  int NOT NULL,
 "date"     timestamp NOT NULL,
 price      decimal(6,2) NOT NULL,
 PRIMARY KEY ( student_id, course_id )
);
CREATE INDEX purchases_course_student ON purchases_course(student_id);
CREATE INDEX purchases_course_course ON purchases_course(course_id);


CREATE TABLE takes_course
(
 student_id int NOT NULL,
 chapter_id int NOT NULL,	
 start_date timestamp NOT NULL,
 end_date   timestamp,
 PRIMARY KEY ( student_id, chapter_id )
);
CREATE INDEX takes_course_student ON takes_course(student_id);
CREATE INDEX takes_course_chapter ON takes_course(chapter_id);


CREATE TABLE chapter
(
 chapter_id serial PRIMARY KEY NOT NULL,
 name       text NOT NULL,
 course_id  int NOT NULL
);
CREATE INDEX chapter_course ON chapter(course_id);
