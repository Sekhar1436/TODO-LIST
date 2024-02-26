import pickle
import os
from datetime import datetime

class Task:
    def __init__(self, description, priority, due_date=None):
        self.description = description
        self.priority = priority
        self.due_date = due_date
        self.completed = False

    def __str__(self):
        status = "Completed" if self.completed else "Pending"
        return f"{self.description} (Priority: {self.priority}, Due Date: {self.due_date}, Status: {status})"

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        self.tasks.remove(task)

    def mark_task_as_completed(self, task):
        task.completed = True

    def list_tasks(self):
        for index, task in enumerate(self.tasks, start=1):
            print(f"{index}. {task}")

    def save_tasks_to_file(self, filename):
        with open(filename, 'wb') as f:
            pickle.dump(self.tasks, f)

    def load_tasks_from_file(self, filename):
        if os.path.exists(filename):
            with open(filename, 'rb') as f:
                self.tasks = pickle.load(f)

def main():
    task_manager = TaskManager()
    task_manager.load_tasks_from_file("tasks.pkl")

    while True:
        print("\nTO-DO LIST APPLICATION")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Mark Task as Completed")
        print("4. List Tasks")
        print("5. Save and Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            description = input("Enter task description: ")
            priority = input("Enter priority (high/medium/low): ")
            due_date_str = input("Enter due date (YYYY-MM-DD) or leave empty: ")
            due_date = datetime.strptime(due_date_str, "%Y-%m-%d") if due_date_str else None
            task = Task(description, priority, due_date)
            task_manager.add_task(task)

        elif choice == "2":
            task_manager.list_tasks()
            index = int(input("Enter the number of the task to remove: ")) - 1
            task_manager.remove_task(task_manager.tasks[index])

        elif choice == "3":
            task_manager.list_tasks()
            index = int(input("Enter the number of the task to mark as completed: ")) - 1
            task_manager.mark_task_as_completed(task_manager.tasks[index])

        elif choice == "4":
            task_manager.list_tasks()

        elif choice == "5":
            task_manager.save_tasks_to_file("tasks.pkl")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
