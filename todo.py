# Dana Abdalkarim - ASAL Training
# CLI To-Do List (OOP Version)

class Task:
    def __init__(self, task_id, description):
        self.id = task_id
        self.description = description
        self.completed = False

    def toggle_status(self):
        self.completed = not self.completed

    def __str__(self):
        status = "Completed" if self.completed else "Pending"
        return f"ID: {self.id} | {self.description} [{status}]"


class TodoManager:
    def __init__(self):
        self.tasks = []
        self._id_counter = 1

    def add_task(self, description):
        new_task = Task(self._id_counter, description)
        self.tasks.append(new_task)
        self._id_counter += 1
        return new_task

    def remove_task(self, task_id):
        for i, task in enumerate(self.tasks):
            if task.id == task_id:
                return self.tasks.pop(i)
        return None

    def get_task(self, task_id):
        return next((t for t in self.tasks if t.id == task_id), None)

    def list_all_tasks(self):
        return self.tasks


class TodoUI:
    def __init__(self):
        self.manager = TodoManager()

    def show_menu(self):
        print("\n===== {CLI To-Do List OOP} =====")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Remove Task")
        print("4. Toggle Task Status")
        print("5. Exit")

    def _get_valid_task_id(self, prompt):


        if not self.manager.list_all_tasks():
            print("The list is empty.")
            return None

        choice = input(prompt).strip()
        if not choice.isdigit():
            print("Invalid input. Please enter a number.")
            return None

        task_id = int(choice)
        task = self.manager.get_task(task_id)
        if not task:
            print(f"No task found with ID {task_id}.")
            return None
        return task_id



    def handle_add(self):
        desc = input("Enter task description: ").strip()
        if desc:
            task = self.manager.add_task(desc)
            print(f"Added: {task.description} (ID: {task.id})")
        else:
            print("Description cannot be empty.")

    def handle_list(self):
        tasks = self.manager.list_all_tasks()
        if not tasks:
            print("No tasks to show.")
        else:
            print("\n--- Current Tasks ---")
            for task in tasks:
                print(task)



    def handle_remove(self):

        self.handle_list()
        task_id = self._get_valid_task_id("Enter Task ID to remove: ")
        if task_id:

            task = self.manager.get_task(task_id)
            confirm = input(f"Delete '{task.description}'? (y/n): ").lower()
            if confirm == 'y':
                self.manager.remove_task(task_id)
                print("Task removed.")

    def handle_toggle(self):
        self.handle_list()
        task_id = self._get_valid_task_id("Enter Task ID to toggle: ")
        if task_id:
            task = self.manager.get_task(task_id)
            task.toggle_status()

            status = "Completed" if task.completed else "Pending"
            print(f"Task is now {status}.")

    def run(self):

        while True:

            self.show_menu()
            choice = input("Choice (1-5): ").strip()
            if choice == "1": self.handle_add()
            elif choice == "2": self.handle_list()
            elif choice == "3": self.handle_remove()
            elif choice == "4": self.handle_toggle()
            elif choice == "5":
                print("Goodbye!")
                break
            else:
                print("Invalid choice.")


if __name__ == "__main__":
    app = TodoUI()
    app.run()