"""
File Operations Module

This module provides functions for reading from and writing to the text file
that stores employee data.
"""
def read_employees():
    # try:
    #     with open(data_dir, 'r') as file: 
    #         # Read lines from the file
    #         lines = file.readlines()
    #         # Process lines to extract employee data
    #         employees_data = [line.strip().split(',') for line in lines]
    #         return employees_data
    # except FileNotFoundError:
    #     print("File not found.")
    #     return []
 def write_employees():
    """
    Write Employees Function

    This function writes employee data to the text file.

    Parameters:
        employees_data (list): A list containing employee data to be written to the text file.
    """
    
    # if not isinstance(employees_data, list):
    #     raise TypeError("employees_data must be a list")

    # for employee in employees_data:
    #     if not isinstance(employee, list) or len(employee)!= 3:
    #         raise ValueError("Each employee must be a list containing three elements")

    # with open(data_dir, 'w') as file:
    #     for employee in employees_data:
    #         file.write(','.join(employee) + '\n')
