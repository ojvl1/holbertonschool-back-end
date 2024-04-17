#!/usr/bin/python3
import requests
import csv
import sys

def fetch_employee_todo_list(employee_id):
    API_info = f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'
    response = requests.get(API_info)
    if response.status_code != 200:
        print("Error:", response.text)
        return

    data = response.json()
    employee_name = data[0]['userId']  # Assuming 'userId' contains the employee's name
    
    completed_tasks = []
    for task in data:
        if task['completed']:
            completed_tasks.append(task['title'])
    
    total_tasks = len(data)

    print(f"Employee {employee_name} is done with tasks({len(completed_tasks)}/{total_tasks}):")
    for task_title in completed_tasks:
        print(f"    {task_title}")

    CSV_file = f"{employee_id}.csv"
    with open(CSV_file, 'w', newline='') as csv_file:
        file_names = ['USER_ID', 'USERNAME', 'TASK_COMPLETE_STATUS', 'TASK_TITLE']
        writer = csv.DictWriter(csv_file, fieldnames=file_names)

        writer.writeheader()
        for task in data:
            writer.writerow({
                'USER_ID': employee_id,
                'USERNAME': task['userId'],
                'TASK_COMPLETED_STATUS': task['completed'],
                'TASK)_TITLE': task['title']
            })

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    fetch_employee_todo_list(employee_id)
