#!/usr/bin/python3
#Python script to return employee's todo lists
#using REST API and returm it to json file

import requests
import sys
import json

def get_employee_todo_list(employee_id):
    base_url = "https://jsonplaceholder.typicode.com"  
    user_url = f"{base_url}/users/{employee_id}"
    todos_url = f"{base_url}/todos?userId={employee_id}"


    user_response = requests.get(user_url)     # Fetch user data
    if user_response.status_code != 200:
        print("Error: Unable to fetch user data")
        return None, None

    user_data = user_response.json()
    employee_name = user_data.get('username')

    
    todos_response = requests.get(todos_url) # Fetch todos data
    if todos_response.status_code != 200:
        print("Error: Unable to fetch todos data")
        return None, None

    todos_data = todos_response.json()
    return employee_name, todos_data

#function to export to json
def export_to_json(employee_id, employee_name, todos_data):
    filename = f"{employee_id}.json"
    todos_list = [
        {"task": task["title"], "completed": task["completed"], "username": employee_name}
        for task in todos_data
    ]
    data = {str(employee_id): todos_list}

    with open(filename, mode='w') as file:
        json.dump(data, file)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 2-export_to_JSON.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Error: Employee ID must be an integer") #check if ID is integer
        sys.exit(1)

    employee_name, todos_data = get_employee_todo_list(employee_id)
    
    if employee_name and todos_data:
        export_to_json(employee_id, employee_name, todos_data)
        print(f"Data exported to {employee_id}.json")
