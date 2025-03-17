import json
import os
import sys
from datetime import datetime

# Name of the JSON file
FILE_NAME = "tasks.json"

# Ensure the JSON file exists or create it if it doesn't
def initialize_json_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w") as file:
            json.dump({"tasks": []}, file, indent=4)

# Read data from JSON file
def read_json_file():
    with open(FILE_NAME, "r") as file:
        return json.load(file)

# Write data to JSON file
def write_json_file(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)

# Add a new task
def add_task(description):
    data = read_json_file()
    created_at = updated_at = datetime.now().isoformat()
    task_id = len(data["tasks"]) + 1
    new_task = {
        "id": task_id,
        "description": description,
        "status": "todo",
        "createdAt": created_at,
        "updatedAt": updated_at
    }
    data["tasks"].append(new_task)
    write_json_file(data)
    print(f"Task added: {description} (ID: {task_id})")

# Update the status of a task
def update_task(task_id, new_status):
    if new_status not in ["todo", "in-progress", "done"]:
        print("Invalid status. Use 'todo', 'in-progress', or 'done'.")
        return
    data = read_json_file()
    for task in data["tasks"]:
        if task["id"] == task_id:
            task["status"] = new_status
            task["updatedAt"] = datetime.now().isoformat()
            write_json_file(data)
            print(f"Task {task_id} updated to status '{new_status}'.")
            return
    print(f"Task with ID {task_id} not found.")

# Delete a task
def delete_task(task_id):
    data = read_json_file()
    for task in data["tasks"]:
        if task["id"] == task_id:
            data["tasks"].remove(task)
            write_json_file(data)
            print(f"Task {task_id} deleted.")
            return
    print(f"Task with ID {task_id} not found.")

# List tasks based on a filter
def list_tasks(filter_status=None):
    data = read_json_file()
    tasks = data["tasks"]
    if filter_status:
        tasks = [task for task in tasks if task["status"] == filter_status]
    if not tasks:
        print("No tasks found.")
        return
    for task in tasks:
        print(f"ID: {task['id']} | Description: {task['description']} | "
              f"Status: {task['status']} | CreatedAt: {task['createdAt']} | "
              f"UpdatedAt: {task['updatedAt']}")

# Command-line interface
def main():
    initialize_json_file()
    if len(sys.argv) < 2:
        print("Usage: python task_manager.py <command> [<args>]")
        return

    command = sys.argv[1]

    if command == "add":
        if len(sys.argv) < 3:
            # Prompt the user for a description
            description = input("Enter task description: ")
            if not description:
                print("Description cannot be empty.")
                return
            add_task(description)
        else:
            # Allow command-line arguments for description
            description = " ".join(sys.argv[2:])
            add_task(description)

    elif command == "update":
        if len(sys.argv) < 4:
            print("Usage: python task_manager.py update <task_id> <status>")
            return
        try:
            task_id = int(sys.argv[2])
        except ValueError:
            print("Task ID must be an integer.")
            return
        new_status = sys.argv[3]
        update_task(task_id, new_status)

    elif command == "delete":
        if len(sys.argv) < 3:
            print("Usage: python task_manager.py delete <task_id>")
            return
        try:
            task_id = int(sys.argv[2])
        except ValueError:
            print("Task ID must be an integer.")
            return
        delete_task(task_id)

    elif command == "list":
        if len(sys.argv) == 3:
            filter_status = sys.argv[2]
            if filter_status not in ["todo", "in-progress", "done"]:
                print("Invalid status. Use 'todo', 'in-progress', or 'done'.")
                return
            list_tasks(filter_status)
        else:
            list_tasks()

    else:
        print(f"Unknown command: {command}")
        print("Available commands: add, update, delete, list")

if __name__ == "__main__":
    main()
