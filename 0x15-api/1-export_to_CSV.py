#!/usr/bin/python3
"""
Python script that exports an employee's todo list data to a CSV file
using a REST API.
"""

import csv
import requests
import sys


def get_employee_todo_list(employee_id):
    """
    Fetches an employee's username and todo list.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        tuple: A tuple containing the employee's username and their todo list.
    """
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employee_id}"
    todos_url = f"{base_url}/todos?userId={employee_id}"

    # Fetch user data
    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        print("Error: Unable to fetch user data")
        return None, None

    user_data = user_response.json()
    employee_name = user_data.get('username')

    # Fetch todos data
    todos_response = requests.get(todos_url)
    if todos_response.status_code != 200:
        print("Error: Unable to fetch todos data")
        return None, None

    todos_data = todos_response.json()
    return employee_name, todos_data


def export_to_csv(employee_id, employee_name, todos_data):
    """
    Exports an employee's todo list data to a CSV file.

    Args:
        employee_id (int): The ID of the employee.
        employee_name (str): The username of the employee.
        todos_data (list): The list of todos.
    """
    filename = f"{employee_id}.csv"

    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in todos_data:
            writer.writerow([employee_id, employee_name, task['completed'], task['title']])


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 1-export_to_CSV.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Error: Employee ID must be an integer")
        sys.exit(1)

    employee_name, todos_data = get_employee_todo_list(employee_id)

    if employee_name and todos_data:
        export_to_csv(employee_id, employee_name, todos_data)
        print(f"Data exported to {employee_id}.csv")
