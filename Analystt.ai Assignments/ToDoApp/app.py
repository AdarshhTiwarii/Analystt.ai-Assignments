class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description=""):
        task = {"title": title, "description": description, "completed": False}
        self.tasks.append(task)
        print(f"Task '{title}' added successfully!")

    def delete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            del self.tasks[task_index]
            print("Task deleted successfully.")
        else:
            print("Invalid task index.")

    def mark_completed(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index]["completed"] = True
            print("Task marked as completed.")
        else:
            print("Invalid task index.")

    def display_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            for index, task in enumerate(self.tasks):
                status = "Completed" if task.get("completed", False) else "Pending"
                print(f"{index + 1}. {task['title']} - {status}")

def main():
    todo_list = ToDoList()

    while True:
        print("\n--- To-Do List ---")
        print("1. Add Task")
        print("2. Delete Task")
        print("3. Mark as Completed")
        print("4. Display Tasks")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description (optional): ")
            todo_list.add_task(title, description)
        elif choice == "2":
            task_index = int(input("Enter task index to delete: ")) - 1
            todo_list.delete_task(task_index)
        elif choice == "3":
            task_index = int(input("Enter task index to mark as completed: ")) - 1
            todo_list.mark_completed(task_index)
        elif choice == "4":
            todo_list.display_tasks()
        elif choice == "5":
            print("Exiting the To-Do List Application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
