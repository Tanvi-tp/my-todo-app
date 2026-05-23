tasks = []

def show_tasks():
    print("\n--- Your Tasks ---")
    if not tasks:
        print("No tasks yet!")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    print("------------------")

def add_task(task):
    tasks.append(task)
    print(f"Task '{task}' added!")

def remove_task(index):
    if 0 < index <= len(tasks):
        removed = tasks.pop(index - 1)
        print(f"Task '{removed}' removed!")
    else:
        print("Invalid task number.")

def clear_tasks():
    tasks.clear()
    print("All tasks cleared!")

def main():
    print("============================")
    print("   Welcome to To-Do App!   ")
    print("============================")
    while True:
        print("\nWhat would you like to do?")
        print("1. View all tasks")
        print("2. Add a task")
        print("3. Remove a task")
        print("4. Clear all tasks")
        print("5. Exit")

        choice = input("\nEnter your choice (1-5): ")

        if choice == "1":
            show_tasks()
        elif choice == "2":
            task = input("Enter task name: ")
            add_task(task)
        elif choice == "3":
            show_tasks()
            index = int(input("Enter task number to remove: "))
            remove_task(index)
        elif choice == "4":
            clear_tasks()
        elif choice == "5":
            print("\nGoodbye! Stay productive!")
            break
        else:
            print("Invalid choice. Please enter 1-5.")

if __name__ == "__main__":
    main()