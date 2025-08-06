# Simple To-Do List Manager in Python

# Store tasks in a list
todo_list = []

# Function to display menu
def display_menu():
    print("\n--- TO-DO LIST MANAGER ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")

# Function to add a task
def add_task():
    task = input("Enter a new task: ")
    todo_list.append({"task": task, "done": False})
    print("Task added successfully!")

# Function to view all tasks
def view_tasks():
    if not todo_list:
        print("No tasks in the list.")
        return
    print("\n--- TASKS ---")
    for idx, item in enumerate(todo_list, start=1):
        status = "✔️" if item["done"] else "❌"
        print(f"{idx}. [{status}] {item['task']}")

# Function to mark a task as done
def mark_done():
    view_tasks()
    try:
        task_no = int(input("Enter task number to mark as done: "))
        if 1 <= task_no <= len(todo_list):
            todo_list[task_no - 1]["done"] = True
            print("Task marked as done!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Function to delete a task
def delete_task():
    view_tasks()
    try:
        task_no = int(input("Enter task number to delete: "))
        if 1 <= task_no <= len(todo_list):
            removed_task = todo_list.pop(task_no - 1)
            print(f"Deleted task: {removed_task['task']}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Main program loop
while True:
    display_menu()
    choice = input("Choose an option (1-5): ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        mark_done()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("Exiting To-Do List Manager. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 5.")
