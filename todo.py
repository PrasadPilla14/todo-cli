# Simple To-Do List CLI
tasks = []

while True:
    print("\n1. Add Task\n2. View Tasks\n3. Remove Task\n4. Exit")
    choice = input("Enter choice: ").strip()  # remove spaces

    if choice == '1':
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added!")
    elif choice == '2':
        print("\nTasks:")
        if not tasks:
            print("No tasks yet!")
        for i, t in enumerate(tasks, 1):
            print(f"{i}. {t}")
    elif choice == '3':
        if not tasks:
            print("No tasks to remove!")
            continue
        num = input("Enter task number to remove: ").strip()
        if not num.isdigit():
            print("Invalid number")
            continue
        num = int(num)
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            print(f"Removed task: {removed}")
        else:
            print("Invalid number")
    elif choice == '4':
        print("Exiting...")
        break
    else:
        print("Invalid choice"