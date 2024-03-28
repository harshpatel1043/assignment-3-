
from collections import defaultdict
from datetime import datetime
import os
"""
Report Generation Module

This module provides a function for generating reports based on employee data.
"""


"""
    Generate Reports Function

    This function generates various reports based on employee data, such as:
    - List of departments
    - List of all employees with ID, full name, and department
    - List of all departments with the average age and salary of employees
    - List of employees in each department with ID, full name, date of birth, salary,
      and total salary for department's employees
    """
    
def calculate_age(date_of_birth):
    """
    Calculate the age based on the date of birth
    """
    today = datetime.today()
    dob = datetime.strptime(date_of_birth, '%Y-%m-%d')
    return today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))


def generate_reports():
    """
    Generate Reports Function

    This function generates various reports based on employee data.
    """
    # Read data from the employees_list.txt file
    current_dir = os.path.dirname(__file__)
    data_dir = os.path.abspath(os.path.join(current_dir, "../data/employees_list.txt"))
   
    with open(data_dir, 'r') as file:
        file.seek(76)


        lines = file.readlines()


    # Initialize data structures for reports
    departments = set()
    employees = defaultdict(list)
    department_employees = defaultdict(list)

    # Parse data and populate reports
    for line in lines[1:]:  # Skip header line
        _, _, _, date_of_birth, _, position, salary = line.strip().split(',')
        first_name, last_name = line.strip().split(',')[1:3]
        department = position

        # Calculate age
        age = calculate_age(date_of_birth)

        # Add department to the set of departments
        departments.add(department)

        # Add employee to the list of employees
        employees[department].append((first_name, last_name, age))

        # Add employee to the list of employees in the department
        department_employees[department].append((first_name, last_name, date_of_birth, salary))

    # Generate reports
    print("List of Departments:")
    for department in departments:
        print(department)

    print("\nList of All Employees with ID, Full Name, and Department:")
    for department, emps in employees.items():
        for emp in emps:
            print(f"{emp[0]} {emp[1]} - Department: {department}")

    print("\nList of All Departments with Average Age and Salary of Employees:")
    for department, emps in employees.items():
        total_age = sum(emp[2] for emp in emps)
        average_age = total_age / len(emps)
        total_salary = sum(float(emp[3]) for emp in department_employees[department])
        average_salary = total_salary / len(department_employees[department])
        print(f"{department}: Average Age: {average_age:.2f}, Average Salary: ${average_salary:.2f}")

    print("\nList of Employees in Each Department with ID, Full Name, Date of Birth, Salary, and Total Salary for Department's Employees:")
    for department, emps in department_employees.items():
        print(f"{department}:")
        for emp in emps:
            print(f"   {emp[0]} {emp[1]}, Date of Birth: {emp[2]}, Salary: ${emp[3]}")
        total_department_salary = sum(float(emp[3]) for emp in emps)
        print(f"   Total Salary for {department}: ${total_department_salary:.2f}")

# Test the function
# generate_reports()

    
