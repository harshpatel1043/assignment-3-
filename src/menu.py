"""
Menu Module

This module provides the main menu interface for the Employee Management System.
Users can interact with the application through the menu options, which include
adding, deleting, updating employee information, generating reports, and exiting
the application.
"""
from .employee_operations import add_employee, delete_employee, update_employee
from .report_generation import generate_reports

def main_menu():
    """
    Main Menu Function
    Displays the main menu for the Employee Management System and prompts the user for input.
    Based on the user's choice, it calls the corresponding functions to perform actions such as
    adding, deleting, or updating employee information, generating reports, or exiting the program.
    """
    while True:
        print("\nEmployee Management System")
        print("1. Add Employee")
        print("2. Delete Employee")
        print("3. Update Employee")
        print("4. Generate Reports")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_employee()
        elif choice == "2":
            delete_employee()
        elif choice == "3":
            update_employee()
        elif choice == "4":
            generate_reports()
        elif choice == "5":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")
