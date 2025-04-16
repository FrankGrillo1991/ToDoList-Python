import os

def clear_screen():
    """Clears the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def display_tasks(tasks):
    """Displays the current to-do list."""
    if not tasks:
        print("No tasks in yout to-do list.")
        return
    
    print("\nYour To-Do List:")
    for index, task in enumerate(tasks):
        status = "[x]" if task["completed"] else "[]"
        print(f"{index + 1}, {status} {task['title']} - {task['description']}")

    def add_task(tasks):
        """Adds a new task to the to-do list."""
        title = input("Enter task title: ")
        description = input("Enter task description: ")
        tasks.append({"title": title, "description": description, "completed": False})
        print("Task added successfully!")

    def mark_complete(tasks):
        """Marks a task as complete"""
        if not tasks:
            print("No tasks to mark complete.")
            return
        
        display_tasks(tasks)
        try:
            task_index = int(input("Enter the number of the task to mark as complete: "))
            if 0 <= task_index < len(tasks):
                tasks[task_index]["completed"] = True
                print("Task marked as complete!")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    def delete_task(tasks):
        """Deletes a task from the to-do list."""
        if not tasks:
            print("No tasks to delete.")
            return
        
        display_tasks(tasks)
        try:
            task_index = int(input("Enter the number of the task to delete: ")) - 1
            if 0 <= task_index < len(tasks):
                del tasks[task_index]
                print("Task deleted successfully!")
            else:
                print("Invalid task number: ")
        except ValueError:
            print("Invalid input. Please enter a number.")

            def main():
                """Main function to run the to-do list"""
                tasks = []
                while True:
                    clear_screen()
                    print("\nTo-Do List Application")
                    print("1. Display Tasks")
                    print("2. Add Task")
                    print("3. Mark as Complete")
                    print("4. Delete Task")
                    print("5. Exit")

                    choice = input("Enter your choice. ")

                    if choice == "1":
                        display_tasks(tasks)
                    elif choice == "2":
                        add_task(tasks)
                    elif choice == "3":
                        mark_complete(tasks)
                    elif choice == "4":
                        delete_task(tasks)
                    elif choice == "5":
                        print("Exiting application. Goodbye!")
                        break
                    else:
                        print("Invalid choice. Please try again.")

                    input("Press Enter to continue...")

                    if __name__ == "__main__":
                        main()