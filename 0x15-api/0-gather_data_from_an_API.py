#!/usr/bin/python3
"""
Python script that returns an employee's todo list
using a REST API.
"""

import json
import requests
import sys


def get_employee_todo_list(employee_id):
    """
    Fetches and prints the todo list progress of a given employee.
    
    Args:
        employee_id (int): The ID of the employee.
    """
    base_url = "https://jsonplaceholder.typicode.com"  # API URL
    user_url = f"{base_url}/users/{employee_id}"
    todos_url = f"{base_url}/todos?userId={employee_id}"

    # Fetches user data
    user_response = requests.get(user_url)
    if user_response.status_code != 200:  # Returns error if unable to fetch user data
        print("Error: Unable to fetch user data")
        return

    user_data = user_response.json()
    employee_name = user_data.get('name')

    # Fetch todos data
    todos_response = requests.get(todos_url)
    if todos_response.status_code != 200:  # Returns error if unable to fetch todos data
        print("Error: Unable to fetch todos data")
        return

    todos_data = todos_response.json()

    # Filter completed and total tasks
    total_tasks = len(todos_data)
    done_tasks = [task for task in todos_data if task['completed']]
    number_of_done_tasks = len(done_tasks)

    # Print the result
    print(f"Employee {employee_name} is done with tasks({number_of_done_tasks}/{total_tasks}):")
    for task in done_tasks:
        print(f"\t {task['title']}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Error: Employee ID must be an integer")
        sys.exit(1)

    get_employee_todo_list(employee_id)
