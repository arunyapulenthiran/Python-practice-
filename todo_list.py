tasks = []

print("To-Do List")
print("----------")

while True:
    print("\n1. Add task")
    print("2. View tasks")
    print("3. Remove task")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        task = input("Enter a task: ")
        tasks.append(task)
        print("Task added.")

    elif choice == "2":
        if not tasks:
            print("No tasks yet.")
        else:
            print("\nYour tasks:")
            for number, task in enumerate(tasks, start=1):
                print(f"{number}. {task}")

    elif choice == "3":
        if not tasks:
            print("No tasks to remove.")
        else:
            for number, task in enumerate(tasks, start=1):
                print(f"{number}. {task}")

            task_number = int(input("Enter the task number to remove: "))

            if 1 <= task_number <= len(tasks):
                removed = tasks.pop(task_number - 1)
                print(f"Removed: {removed}")
            else:
                print("Invalid task number.")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid option. Please try again.")
