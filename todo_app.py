# Simple Todo List Application
# This application has intentional bugs for debugging practice

class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        """Add a new task to the list"""
        self.tasks.append(task)
        print(f"Task '{task}' added successfully!")

    def remove_task(self, task_index):
        """Remove a task by index"""
        if 0 <= task_index < len(self.tasks):
            removed_task = self.tasks[task_index]
            del self.tasks[task_index]
            print(f"Task '{removed_task}' removed!")
        else:
            print(f"Error: Invalid index {task_index}. Please enter a valid task number.")
    def view_tasks(self):
        """Display all tasks"""
        if len(self.tasks) == 0:  # BUG 2: Using = instead of ==
            print("No tasks in the list!")
        else:
            print("\nYour Todo List:")
            for i, task in enumerate(self.tasks):
                print(f"{i}. {task}")

    def mark_complete(self, task_index):
        """Mark a task as complete"""
        # BUG 3: Logic error - doesn't actually mark anything, just prints
        print(f"Task {task_index} marked as complete!")

    def get_task_count(self):
        """Return the number of tasks"""
        return len(self.task)  # BUG 4: Typo - should be self.tasks

def main():
    todo = TodoList()

    while True:
        print("\n=== Todo List Menu ===")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Mark Complete")
        print("5. Task Count")
        print("6. Exit")

        choice = input("\nEnter your choice (1-6): ")

        if choice == "1":
            task = input("Enter task description: ")
            todo.add_task(task)

        elif choice == "2":
            todo.view_tasks()

        elif choice == "3":
            todo.view_tasks()
            index = int(input("Enter task index to remove: "))
            todo.remove_task(index)

        elif choice == "4":
            todo.view_tasks()
            index = int(input("Enter task index to mark complete: "))
            todo.mark_complete(index)

        elif choice == "5":
            count = todo.get_task_count()
            print(f"You have {count} tasks.")

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
