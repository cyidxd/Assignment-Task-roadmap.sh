Task Manager CLI Application
A simple Command-Line Interface (CLI) tool to manage tasks. Tasks are stored in a JSON file and include properties like description, status, and timestamps.

Features
Add tasks with unique IDs and descriptions.

Update task status (todo, in-progress, done).

Delete tasks by ID.

List all tasks or filter tasks by status.

Task Properties
Each task contains:

id: A unique identifier for the task.

description: Task description.

status: Current status (todo, in-progress, done).

createdAt: Timestamp for task creation.

updatedAt: Timestamp for the last update.

Usage
Run the script and use commands:

Add a task: Add a new task with a description.

Update task status: Change the status of a task by its ID.

Delete a task: Remove a task from the list by ID.

List tasks: View all tasks or filter them based on their status (todo, in-progress, or done).

How It Works
The program creates a JSON file named tasks.json to store task data.

Each task includes all required properties such as ID, description, and timestamps.

Users can interact with the application entirely from the command line.

This Task Manager is simple yet effective for managing and tracking your tasks directly through the terminal.
