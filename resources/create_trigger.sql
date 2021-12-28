CREATE OR REPLACE FUNCTION change_modification_date() RETURNS TRIGGER LANGUAGE plpgsql  AS
$$ BEGIN
	NEW.modification_date = NOW();
	RETURN NEW;
END; $$;


CREATE TRIGGER assistant_update_modification_date
  BEFORE UPDATE
  ON assistant
  FOR EACH ROW
  EXECUTE PROCEDURE change_modification_date();
  
CREATE TRIGGER category_update_modification_date
  BEFORE UPDATE
  ON category
  FOR EACH ROW
  EXECUTE PROCEDURE change_modification_date();
  
CREATE TRIGGER subcategory_update_modification_date
  BEFORE UPDATE
  ON subcategory
  FOR EACH ROW
  EXECUTE PROCEDURE change_modification_date();
  
CREATE TRIGGER topic_update_modification_date
  BEFORE UPDATE
  ON topic
  FOR EACH ROW
  EXECUTE PROCEDURE change_modification_date();
  
CREATE TRIGGER university_update_modification_date
  BEFORE UPDATE
  ON university
  FOR EACH ROW
  EXECUTE PROCEDURE change_modification_date();
  
CREATE TRIGGER instructor_update_modification_date
  BEFORE UPDATE
  ON instructor
  FOR EACH ROW
  EXECUTE PROCEDURE change_modification_date();
  
CREATE TRIGGER instructor_rating_update_modification_date
  BEFORE UPDATE
  ON instructor_rating
  FOR EACH ROW
  EXECUTE PROCEDURE change_modification_date();
  
CREATE TRIGGER course_update_modification_date
  BEFORE UPDATE
  ON course
  FOR EACH ROW
  EXECUTE PROCEDURE change_modification_date();
  
CREATE TRIGGER course_rating_update_modification_date
  BEFORE UPDATE
  ON course_rating
  FOR EACH ROW
  EXECUTE PROCEDURE change_modification_date();
  
CREATE TRIGGER student_update_modification_date
  BEFORE UPDATE
  ON student
  FOR EACH ROW
  EXECUTE PROCEDURE change_modification_date();