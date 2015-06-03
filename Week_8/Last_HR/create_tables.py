import sqlite3


connection = sqlite3.connect("hr.db")
cursor = connection.cursor()


CREATE_STUDENTS_TABLE = """
CREATE TABLE IF NOT EXISTS Students(
    id INTEGER PRIMARY KEY,
    name TEXT,
    github TEXT
)
"""


CREATE_COURSES_TABLE = """
CREATE TABLE IF NOT EXISTS Courses(
    id INTEGER PRIMARY KEY,
    name TEXT
)
"""

TABLE_STUDENTS_TO_COURSES = """
CREATE TABLE IF NOT EXISTS Students_to_Courses(
    student_id INTEGER,
    course_id INTEGER,
    FOREIGN KEY(student_id) REFERENCES Students(id),
    FOREIGN KEY(course_id) REFERENCES Courses(id)
)
"""

for create_table in [CREATE_STUDENTS_TABLE, CREATE_COURSES_TABLE, TABLE_STUDENTS_TO_COURSES]:
    cursor.execute(create_table)

connection.commit()

connection.close()
