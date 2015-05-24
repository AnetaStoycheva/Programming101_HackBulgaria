import sqlite3

connection = sqlite3.connect("company.db")
cursor = connection.cursor()


class CliInterface:
    def __init__(self):
        pass

    def start(self):
        print("Welcome to our company's database manager.")

        while True:
            command = input("Enter command > ")
            try:
                self.__command_dispatcher(command)
            except Exit:
                break

    def __command_dispatcher(self, command):
        parts = command.split(" ")

        if parts[0] == "list_employees":
            list_employees()

        elif parts[0] == "monthly_spending":
            print("The company is spending ${} for a month.".format(monthly_spending()))

        elif parts[0] == "yearly_spending":
            print("The company is spending ${} for an year.".format(yearly_spending()))

        elif parts[0] == "add_employee":
            name = input("Name ")
            salary = int(input("monthly_salary: "))
            bonus = int(input("yearly_bonus: "))
            position = input("position: ")
            print(add_employee(name, salary, bonus, position))

        elif parts[0] == "delete_employee":
            id_employee = int(input("employee_id: "))
            print(delete_employee(id_employee))

        elif parts[0] == "update_employee":
            name = input("Name ")
            salary = int(input("monthly_salary: "))
            bonus = int(input("yearly_bonus: "))
            position = input("position: ")
            print(update_employee(name, salary, bonus, position, parts[1]))

        elif parts[0] == 'exit':
            raise Exit

        elif parts[0] == "help":
            print("These are possible commands:\nlist_employees,\n\
monthly_spending,\nyearly_spending,\nadd_employee,\ndelete_employee,\n\
update_employee,\nexit")

        else:
            print('Not a valid command')


class Exit(Exception):
    pass


def list_employees():
    query = """
SELECT name, position
FROM employees
"""
    cursor_result = cursor.execute(query)
    result = cursor_result.fetchall()
    for element in result:
        print(element[0] + " - " + element[1])


def monthly_spending():
    query = """
SELECT monthly_salary
FROM employees
"""
    cursor_result = cursor.execute(query)
    result = cursor_result.fetchall()
    total = 0
    for element in result:
        total += element[0]
    return total


def yearly_spending():
    query = """
SELECT monthly_salary, yearly_bonus
FROM employees
"""
    cursor_result = cursor.execute(query)
    result = cursor_result.fetchall()
    total = 0
    for element in result:
        total += (element[0] * 12) + element[1]
    return total


def add_employee(name, salary, bonus, position):
    query = """
INSERT INTO employees(name, monthly_salary, yearly_bonus, position)
VALUES(?, ?, ?, ?)
"""
    cursor_result = cursor.execute(query, (name, salary, bonus, position))
    connection.commit()


def delete_employee(employee_id):
    query = """
DELETE FROM employees
WHERE id = ?
"""
    cursor_result = cursor.execute(query, (employee_id, ))
    connection.commit()


def update_employee(name, salary, bonus, position, id):
    query = """
UPDATE employees
SET name = ?,
    monthly_salary = ?,
    yearly_bonus = ?,
    position = ?
WHERE id = ?
"""
    cursor_result = cursor.execute(query, (name, salary, bonus, position, id))
    connection.commit()


def main():
    cli = CliInterface()
    cli.start()


if __name__ == '__main__':
    main()
