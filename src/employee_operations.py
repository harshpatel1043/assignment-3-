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

    # print(data_dir)
    with open(data_dir, 'a') as file:
        file.write(f"{get_last_id() + 1},{first_name},{last_name},{date_of_birth},{start_year},{position},{salary}\n")
    # print(lines)
    # with open(data_dir, 'a') as file:
    #     # file.write(f"{get_last_id() + 1},{first_name},{last_name},{date_of_birth},{start_year},{position},{salary}\n")
    #     first_line= file.readline()
    # print(first_line)
    # while True:
    #     pass
def delete_employee():
    """
    Delete Employee Function

    This function prompts the user to input the ID of the employee to be deleted and
    removes the employee from the system.

    """
    # Prompt the user to input the ID of the employee to be deleted
    employee_id = input("Enter the ID of the employee to be deleted: ")

    # Read all lines from the file except the one with the specified employee ID
    current_dir = os.path.dirname(__file__)
    data_dir = os.path.abspath(os.path.join(current_dir, "../data/employees_list.txt"))
    with open(data_dir, 'r') as file:
        lines = file.readlines()
    with open('employees_list.txt', 'w') as file:
        for line in lines:
            if not line.startswith(employee_id + ','):
                file.write(line)

def update_employee():
    """
    Update Employee Function

    This function prompts the user to input the ID of the employee to be updated and
    allows the user to modify the employee's information such as name, department, or salary.

    """

    
    # Prompt the user to input the ID of the employee to be updated
    employee_id = int(input("Enter the ID of the employee to be updated: "))

    # Find the employee with the given ID
    employee = next((employee for employee in employee if employee.id == employee_id), None)

    # Check if the employee exists
    if employee:
        # Prompt the user to input the new name, department, and salary
        name = input("Enter the new name: ")
        department = input("Enter the new department: ")
        salary = float(input("Enter the new salary: "))

        # Update the employee's information
        employee.name = name
        employee.department = department
        employee.salary = salary

        # Print a success message
        print(f"Employee {employee_id} has been updated.")
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