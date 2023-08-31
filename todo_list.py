class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task_name, due_date):
        self.tasks.append({"name": task_name, "due_date": due_date, "complete": False})

    def mark_task_complete(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index]["complete"] = True

    def list_tasks(self):
        for index, task in enumerate(self.tasks):
            status = "✓" if task["complete"] else " "
            print(f"{index + 1}. [{status}] {task['name']} (Due: {task['due_date']})")

def main():
    todo_list = ToDoList()

    while True:
        print("\n--- To-Do List ---")
        print("1. Add Task")
        print("2. Mark Task as Complete")
        print("3. List Tasks")
        print("4. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            task_name = input("Enter task name: ")
            due_date = input("Enter due date: ")
            todo_list.add_task(task_name, due_date)
        elif choice == "2":
            task_index = int(input("Enter task index to mark as complete: ")) - 1
            todo_list.mark_task_complete(task_index)
        elif choice == "3":
            todo_list.list_tasks()
        elif choice == "4":
            print("Exiting the To-Do List application.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
