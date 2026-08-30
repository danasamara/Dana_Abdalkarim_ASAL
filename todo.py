# Dana Abdalkarim - ASAL Training
# CLI To-Do List (basic)
# Using functions, loops, lists, and dictionaries.

tasks = []

def show_menu():
    print("\n===== {CLI To-Do List} =====")
    print("1. Add Task")
    print("2. List Tasks")
    print("3. Remove Task")
    print("4. Mark Task as Completed / Pending")
    print("5. Exit")

def add_task():
    description = input("Enter task description: ").strip()
    if description == "":
        print("Task description cannot be empty.")
        return
    task = {
        "description": description,
        "completed": False
    }
    tasks.append(task)
    print("Task added successfully.")

def list_tasks():
    if len(tasks) == 0:
        print("No tasks yet.")
        return

    print("\n----- Your Tasks -----")
    for index, task in enumerate(tasks):
        number = index + 1
        if task["completed"]:
            status = "Completed"
        else:
            status = "Pending"
        print(f"{number}. {task['description']} [{status}]")


def remove_task():
    if len(tasks) == 0:
        print("No tasks to remove.")
        return

    list_tasks()
    choice = input("Enter the task number to remove: ").strip()

    if not choice.isdigit():
        print("Please enter a valid number.")
        return
    task_number = int(choice)
    if task_number < 1 or task_number > len(tasks):
        print("That task number does not exist.")
        return
    removed_task = tasks.pop(task_number - 1)
    print(f"Removed: {removed_task['description']}")


def mark_task():
    if len(tasks) == 0:
        print("No tasks to update.")
        return

    list_tasks()
    choice = input("Enter the task number to update: ").strip()

    if not choice.isdigit():
        print("Please enter a valid number.")
        return
    task_number = int(choice)
    if task_number < 1 or task_number > len(tasks):
        print("That task number does not exist.")
        return

    task = tasks[task_number - 1]
    if task["completed"]:
        task["completed"] = False
        print(f"'{task['description']}' is now Pending.")
    else:
        task["completed"] = True
        print(f"'{task['description']}' is now Completed.")


def main():
    while True:
        show_menu()
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            add_task()
        elif choice == "2":
            list_tasks()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            mark_task()
        elif choice == "5":
            print("Exiting!")
            break
        else:
            print("Invalid option. Please choose 1, 2, 3, 4, or 5.")


if __name__ == "__main__":
    main()
