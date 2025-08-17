# Simple To-Do List in Python

todo_list = []

def show_tasks():
    if not todo_list:
        print("✅ No tasks in the list!")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(todo_list, 1):
            print(f"{i}. {task}")

def add_task(task):
    todo_list.append(task)
    print(f"Task '{task}' added!")

def remove_task(index):
    try:
        removed = todo_list.pop(index - 1)
        print(f"Task '{removed}' removed!")
    except IndexError:
        print("❌ Invalid task number!")

while True:
    print("\n--- TO-DO LIST MENU ---")
    print("1. Show Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter choice (1-4): ")

    if choice == "1":
        show_tasks()
    elif choice == "2":
        task = input("Enter a new task: ")
        add_task(task)
    elif choice == "3":
        show_tasks()
        try:
            index = int(input("Enter task number to remove: "))
            remove_task(index)
        except ValueError:
            print("❌ Please enter a valid number!")
    elif choice == "4":
        print("👋 Exiting To-Do List. Goodbye!")
        break
    else:
        print("❌ Invalid choice, please try again.")
