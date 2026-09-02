# Dana Abdalkarim - ASAL Training
# CLI To-Do List (Refactored)

# Global State
tasks = []
task_id_counter = 1



def create_task(task_id, description):
    return {
        "id": task_id,
        "description": description,
        "completed": False
    }


def add_task_logic(description):
    global task_id_counter
    new_task = create_task(task_id_counter, description)
    tasks.append(new_task)
    task_id_counter += 1
    return new_task


def remove_task_logic(task_id):
    global tasks
    for i, task in enumerate(tasks):
        if task["id"] == task_id:
            return tasks.pop(i)
    return None


def toggle_task_logic(task_id):
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = not task["completed"]
            return task
    return None


def get_task_by_id(task_id):
    return next((t for t in tasks if t["id"] == task_id), None)







def show_menu():
    print("\n===== {CLI To-Do List} =====")
    print("1. Add Task")
    print("2. List Tasks")
    print("3. Remove Task")
    print("4. Mark Task as Completed / Pending")
    print("5. Exit")


def list_tasks():
    if not tasks:
        print("No tasks yet.")
        return

    print("\n----- Your Tasks -----")
    for task in tasks:
        status = "Completed" if task["completed"] else "Pending"
        print(f"ID: {task['id']} | {task['description']} [{status}]")


def validate_task_input(prompt):

    if not tasks:
        print("The list is currently empty.")
        return None

    choice = input(prompt).strip()
    if not choice.isdigit():
        print("Invalid input. Please enter a numeric ID.")
        return None

    task_id = int(choice)
    task = get_task_by_id(task_id)

    if not task:
        print(f"Task with ID {task_id} does not exist.")
        return None

    return task_id




def handle_add_task():
    description = input("Enter task description: ").strip()
    if not description:
        print("Task description cannot be empty.")
        return

    task = add_task_logic(description)
    print(f"Task added successfully (ID: {task['id']}).")


def handle_remove_task():
    list_tasks()
    task_id = validate_task_input("Enter the task ID to remove: ")

    if task_id is not None:
        task = get_task_by_id(task_id)
        confirm = input(f"Are you sure you want to delete '{task['description']}'? (y/n): ").lower()
        if confirm == 'y':
            removed = remove_task_logic(task_id)
            print(f"Removed: {removed['description']}")
        else:
            print("Deletion cancelled.")


def handle_mark_task():
    list_tasks()
    task_id = validate_task_input("Enter the task ID to update: ")

    if task_id is not None:
        task = toggle_task_logic(task_id)
        status = "Completed" if task["completed"] else "Pending"
        print(f"'{task['description']}' is now {status}.")


def main():
    while True:
        show_menu()
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            handle_add_task()
        elif choice == "2":
            list_tasks()
        elif choice == "3":
            handle_remove_task()
        elif choice == "4":
            handle_mark_task()
        elif choice == "5":
            print("Exiting!")
            break
        else:
            print("Invalid option. Please choose 1-5.")


if __name__ == "__main__":
    main()