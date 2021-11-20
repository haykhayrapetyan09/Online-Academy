CREATE OR REPLACE PROCEDURE increment_university(given_university_id int) LANGUAGE plpgsql AS
$$ BEGIN
	UPDATE university
	SET total_instructors = total_instructors+1
	WHERE university_id = given_university_id;
END; $$;

CREATE OR REPLACE PROCEDURE increment_instructor(given_instructor_id int) LANGUAGE plpgsql AS
$$ BEGIN
	UPDATE instructor
	SET total_courses = total_courses+1
	WHERE instructor_id = given_instructor_id;
END; $$;

CREATE OR REPLACE PROCEDURE increment_assistant(given_assistant_id int) LANGUAGE plpgsql AS
$$ BEGIN
	UPDATE assistant
	SET total_courses = total_courses+1
	WHERE assistant_id = given_assistant_id;
END; $$;

CREATE OR REPLACE PROCEDURE increment_topic(given_topic_id int) LANGUAGE plpgsql AS
$$ BEGIN
	UPDATE topic
	SET total_courses = total_courses+1
	WHERE topic_id = given_topic_id;
END; $$;

CREATE OR REPLACE PROCEDURE increment_course(given_course_id int) LANGUAGE plpgsql AS
$$ BEGIN
	UPDATE course
	SET total_chaptser = total_chapters+1
	WHERE course_id = given_course_id;
END; $$;
