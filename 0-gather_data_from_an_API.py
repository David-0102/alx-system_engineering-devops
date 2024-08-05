#!/usr/bin/python3
import requests
import sys

def gather_data(employee_id):
    base_url = "https://jsonplaceholder.typicode.com"
    
    # Fetch employee details
    user_url = f"{base_url}/users/{employee_id}"
    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        print(f"User with ID {employee_id} not found.")
        return
    
    user_data = user_response.json()
    employee_name = user_data.get("name")

    # Fetch employee TODO list
    todos_url = f"{base_url}/todos?userId={employee_id}"
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    # Process TODO list
    total_tasks = len(todos_data)
    done_tasks = [task for task in todos_data if task.get("completed")]
    number_of_done_tasks = len(done_tasks)

    # Display the results
    print(f"Employee {employee_name} is done with tasks({number_of_done_tasks}/{total_tasks}):")
    for task in done_tasks:
        print(f"\t {task.get('title')}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
    else:
        try:
            employee_id = int(sys.argv[1])
            gather_data(employee_id)
        except ValueError:
            print("Employee ID must be an integer.")

