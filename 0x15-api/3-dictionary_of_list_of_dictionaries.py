#!/usr/bin/env python3
"""
Script that uses the REST API to return information about an employee's
TODO list progress and export data in JSON format.
"""

import json
import requests

def fetch_todos_and_users():
    """
    Fetch the TODO list and user details from the JSONPlaceholder API.

    Returns:
        tuple: A tuple containing a list of todos and a list of users.
    """
    todos_response = requests.get("https://jsonplaceholder.typicode.com/todos")
    users_response = requests.get("https://jsonplaceholder.typicode.com/users")

    todos = todos_response.json()
    users = users_response.json()

    return todos, users

def create_user_dict(users):
    """
    Create a dictionary with user ID as the key and user details as the value.

    Args:
        users (list): List of user details.

    Returns:
        dict: A dictionary with user IDs as keys and user details as values.
    """
    user_dict = {}
    for user in users:
        user_dict[user['id']] = user
    return user_dict

def create_todo_dict(todos, user_dict):
    """
    Create a dictionary of lists of dictionaries with tasks for each user.

    Args:
        todos (list): List of todos.
        user_dict (dict): Dictionary of user details.

    Returns:
        dict: A dictionary with user IDs as keys and lists of todo dictionaries as values.
    """
    todo_dict = {}
    for todo in todos:
        user_id = todo['userId']
        username = user_dict[user_id]['username']
        task_info = {
            "username": username,
            "task": todo['title'],
            "completed": todo['completed']
        }
        if user_id not in todo_dict:
            todo_dict[user_id] = []
        todo_dict[user_id].append(task_info)
    return todo_dict

def export_to_json(data, filename):
    """
    Export the data to a JSON file.

    Args:
        data (dict): The data to export.
        filename (str): The name of the file to export to.
    """
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)

def main():
    """
    Main function to fetch data, process it, and export it to a JSON file.
    """
    todos, users = fetch_todos_and_users()
    user_dict = create_user_dict(users)
    todo_dict = create_todo_dict(todos, user_dict)
    export_to_json(todo_dict, 'todo_all_employees.json')

if __name__ == "__main__":
    main()
