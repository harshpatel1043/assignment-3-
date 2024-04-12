"""
Employee Operations Module

This module provides functions for adding, deleting, and updating employee information.
"""

import os

def add_employee():

    
    """
    Add Employee Function

    This function prompts the user to input details for a new employee and adds the employee
    to the system.

    """
    first_name = input("Enter the first name of the new employee: ")
    last_name = input("Enter the last name of the new employee: ")
    date_of_birth = input("Enter the date of birth (YYYY-MM-DD) of the new employee: ")
    start_year = int(input("Enter the start year of the new employee: "))
    position = input("Enter the position of the new employee: ")
    salary = float(input("Enter the salary of the new employee: "))
    current_dir = os.path.dirname(__file__)
    data_dir = os.path.abspath(os.path.join(current_dir, "../data/employees_list.txt"))


    with open(data_dir, 'a') as file:
        file.write(f"{get_last_id() + 1},{first_name},{last_name},{date_of_birth},{start_year},{position},{salary}\n")

def delete_employee():
    """
    Delete Employee Function

    This function prompts the user to input the ID of the employee to be deleted and
    removes the employee from the system.

    """

    employee_id = input("Enter the ID of the employee to be deleted: ")

    current_dir = os.path.dirname(__file__)
    data_dir = os.path.abspath(os.path.join(current_dir, "../data/employees_list.txt"))

    # Load existing employees data
    employees = []
    with open(data_dir, 'r') as file:
        for line in file:
            employee_data = line.strip().split(',')
            employees.append(Employee(*employee_data))

    # Find the index of the employee with the given ID
    employee_index = None
    for i, emp in enumerate(employees):
        if emp.id == employee_id:
            employee_index = i
            break

    # Check if the employee exists
    if employee_index is not None:
        # Remove the employee from the list
        del employees[employee_index]

        # Save the updated data back to the file
        with open(data_dir, 'w') as file:
            for emp in employees:
                file.write(f"{emp.id},{emp.first_name},{emp.last_name},{emp.date_of_birth},{emp.start_year},{emp.position},{emp.salary}\n")

        # Print a success message
        print(f"Employee {employee_id} has been deleted.")
    else:
        # Print an error message if the employee does not exist
        print(f"Employee {employee_id} not found.")

def update_employee():
    """
    Update Employee Function

    This function prompts the user to input the ID of the employee to be updated and
    allows the user to modify the employee's information such as name, department, or salary.

    """
    current_dir = os.path.dirname(__file__)
    data_dir = os.path.abspath(os.path.join(current_dir, "../data/employees_list.txt"))

    employee_id = int(input("Enter the ID of the employee to be updated: "))

    # Find the employee with the given ID
    employee = next((emp for emp in employees if emp.id == employee_id), None)

    # Check if the employee exists
    if employee:
        # Prompt the user to input the new department and salary
        department = input("Enter the new department: ")
        salary = float(input("Enter the new salary: "))

        # Update the employee's department and salary
        employee.department = department
        employee.salary = salary

        # Print a success message
        print(f"Employee {employee_id} has been updated.")

        # Save the updated data back to the file
        with open(data_dir, 'w') as file:
            for emp in employees:
                file.write(f"{emp.id},{emp.first_name},{emp.last_name},{emp.date_of_birth},{emp.start_year},{emp.position},{emp.salary}\n")
    else:
        # Print an error message if the employee does not exist
        print(f"Employee {employee_id} not found.")
    


def get_last_id():
    """
    Get the ID of the last employee in the system
    """
    current_dir = os.path.dirname(__file__)
    data_dir = os.path.abspath(os.path.join(current_dir, "../data/employees_list.txt"))
    with open(data_dir, 'r') as file:
        lines = file.readlines()
    if lines:
        last_line = lines[-1].strip().split(',')
        return int(last_line[0])
    else:
        return 0