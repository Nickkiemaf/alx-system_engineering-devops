#!/usr/bin/env python3

#Script that, using this REST API, for a given employee ID, returns
#information about his/her TODO list progress
#and export data in the JSON format.


import json
import requests

def fetch_todos_and_users():
    todos_response = requests.get("https://jsonplaceholder.typicode.com/todos")
    users_response = requests.get("https://jsonplaceholder.typicode.com/users")

    todos = todos_response.json()
    users = users_response.json()

    return todos, users

def create_user_dict(users):
    user_dict = {}
    for user in users:
        user_dict[user['id']] = user
    return user_dict

def create_todo_dict(todos, user_dict):
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
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)

def main():
    todos, users = fetch_todos_and_users()
    user_dict = create_user_dict(users)
    todo_dict = create_todo_dict(todos, user_dict)
    export_to_json(todo_dict, 'todo_all_employees.json')

if __name__ == "__main__":
    main()
