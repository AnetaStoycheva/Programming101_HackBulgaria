import sqlite3


connection = sqlite3.connect("hr.db")
cursor = connection.cursor()


class CliInterface:
    def __init__(self):
        pass

    def start(self):
        print("Welcome! You're the last HR :(")

        while True:
            command = input("Enter command > ")
            try:
                self.__command_dispatcher(command)
            except Exit:
                break

    def __command_dispatcher(self, command):
        parts = command.split(" ")

        if parts[0] == "show_students":
            show_students()

        elif parts[0] == "show_courses":
            print("All courses are: ")
            show_courses()

        elif parts[0] == "courses_with_students":
            print("For each student - list the courses he has attending")
            courses_with_students()

        elif parts[0] == "the_smartest_students":
            the_smartest_students()

        elif parts[0] == 'exit':
            raise Exit

        elif parts[0] == "help":
            print("These are possible commands:\nshow_students,\n\
show_courses,\ncourses_with_students,\nthe_smartest_students,\nexit")

        else:
            print('Not a valid command')


class Exit(Exception):
    pass

# List all students with their GitHub accounts
students_query = """
    SELECT students.name, github
    FROM Students
"""


def show_students():
    cursor.execute(students_query)
    rows = cursor.fetchall()
    for row in rows:
        print(row[0], row[1])


# List all courses
courses_query = """
    SELECT courses.name
    FROM Courses
"""


def show_courses():
    cursor.execute(courses_query)
    rows = cursor.fetchall()
    for row in rows:
        print(row[0])


# List all students and for each student - list the courses he attended
student_courses_query = """
    SELECT students.name, course_id, courses.name
    FROM Students
    JOIN Students_to_Courses
    ON Students.id = student_id
    JOIN Courses
    ON Courses.id = course_id
"""


def courses_with_students():
    cursor.execute(student_courses_query)
    rows = cursor.fetchall()
    dictionary = {}
    for row in rows:
        if row[0] not in dictionary:
            dictionary[row[0]] = []
        dictionary[row[0]].append(row[2])

    for element in dictionary:
        print(element + ': ' + ', '.join(dictionary[element]))


# Find the students that have attented the most courses in Hack Bulgaria.
# The github account is from me ;)
# Because I'm the best HR :)
the_most_courses = """
    SELECT students.name, COUNT(course_id) AS course_count, github
    FROM Students
    JOIN Students_to_Courses
    ON Students.id = student_id
    GROUP BY id
    ORDER BY course_count DESC
"""


def the_smartest_students():
    cursor.execute(the_most_courses)
    rows = cursor.fetchmany(5)
    for row in rows:
        print(row[0], row[2] + ', courses: ' + str(row[1]))


def main():
    new = CliInterface()
    new.start()


if __name__ == '__main__':
    main()
