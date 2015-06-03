import requests
import sqlite3


api_url = 'https://hackbulgaria.com/api/students/'
students_data = requests.get(api_url).json()
# print(students_data)


connection = sqlite3.connect("hr.db")
cursor = connection.cursor()


def insert_student(connection, cursor, student):
    insert_query = """
        INSERT INTO Students(name, github)
        VALUES(?, ?)
    """
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    cursor.execute(insert_query, (student['name'], student['github']))  # tuk pi6em stojnostite, s koito zamestvame ?te
    connection.commit()
    return cursor.lastrowid  # vry6ta poslednoto id, koeto sme vkarali s INSERT zaqvka


def insert_course(connection, cursor, course):
    insert_query = """
        INSERT INTO Courses(name)
        VALUES(?)
    """

    cursor.execute(insert_query, (course['name'],))
    connection.commit()
    return cursor.lastrowid


def create_relation(connection, cursor, student_id, course_id):
    insert_query = """
        INSERT INTO Students_to_Courses(student_id, course_id)
        VALUES(?, ?)
    """

    cursor.execute(insert_query, (student_id, course_id))
    connection.commit()
    return cursor.lastrowid


"""re4nik, k sypostavq id na curs spored imeto mu"""
from_course_name_to_id = {}

for student in students_data:
    st_id = insert_student(connection, cursor, student)
    courses = student['courses']  # za6toto taka sa zapisani v json-a ni
    for course in courses:
        if course['name'] in from_course_name_to_id:
            course_id = from_course_name_to_id[course['name']]
        else:
            course_id = insert_course(connection, cursor, course)
            from_course_name_to_id[course['name']] = course_id

        create_relation(connection, cursor, st_id, course_id)

    print('Added student: ' + student['name'])


connection.close()
