#!/usr/bin/python3
"""
1-export_to_CSV.py

fetches TODO list data for a given employee ID from the JSONPlaceholder API
Dependencies:
    - requests: To make HTTP requests to the JSONPlaceholder API.
    - csv: To write data to a CSV file.
    - sys: To handle command-line arguments.

Note:
    - Ensure script has execute permissions to run directly from command line.
"""
import csv
import requests
import sys


def export_to_csv(employee_id):
    base_url = "https://jsonplaceholder.typicode.com"

    # Fetch employee details
    user_url = f"{base_url}/users/{employee_id}"
    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        print(f"User with ID {employee_id} not found.")
        return

    user_data = user_response.json()
    username = user_data.get("username")

    # Fetch employee TODO list
    todos_url = f"{base_url}/todos?userId={employee_id}"
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    # Prepare data for CSV
    csv_filename = f"{employee_id}.csv"
    with open(csv_filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in todos_data:
            user_id = task.get("userId")
            task_title = task.get("title")
            task_completed_status = str(task.get("completed")).lower()
            writer.writerow([
                user_id,
                username,
                task_completed_status,
                task_title
             ])

    print(f"Data exported to {csv_filename}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./1-export_to_CSV.py <employee_id>")
    else:
        try:
            employee_id = int(sys.argv[1])
            export_to_csv(employee_id)
        except ValueError:
            print("Employee ID must be an integer.")
