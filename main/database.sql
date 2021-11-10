CREATE TABLE IF NOT EXISTS people{
    person_id INT PRIMARY KEY,
    first_name varchar(30) NOT NULL,
    last_name varchar(30) NOT NULL,
    birth_date DATE,
    gender varchar(1),
    phone_number INT,
    email varchar(50)
};

CREATE TABLE IF NOT EXISTS sections{
    section_id INT PRIMARY KEY,
    section_name VARCHAR(20) NOT NULL,
    mayor_id INT,
    vice_mayor_id INT
};

CREATE TABLE IF NOT EXISTS students{
    student_id INT UNIQUE,
    section_id INT
};

ALTER TABLE sections
ADD FOREIGN KEY(mayor_id)
REFERENCE students(student_id)
ON DELETE SET NULL;

ALTER TABLE sections
ADD FOREIGN KEY(vice_mayor_id)
REFERENCE students(student_id)
ON DELETE SET NULL;

ALTER TABLE students
ADD FOREIGN KEY(student_id)
REFERENCE people(person_id)
ON DELETE CASCADE;

ALTER TABLE students
ADD FOREIGN KEY(section_id)
REFERENCE sections(section_id)
ON DELETE SET NULL;

