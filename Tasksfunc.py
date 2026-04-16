def view():
    try:
        with open("Tasks.txt", "r") as f:
            tasks = f.readlines()

            if not tasks:
                print("No tasks found.")
                return

            print("\nYour Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task.strip()}")

    except FileNotFoundError:
        print("No tasks file found. Add a task first.")
def add():
    task = input("Enter new task: ").strip()

    if not task:
        print("Task cannot be empty.")
        return

    with open("Tasks.txt", "a") as f:
        f.write(f"[ ] {task}\n")

    print("Task added successfully.")
  def mark():
    try:
        with open("Tasks.txt", "r") as f:
            tasks = f.readlines()

        if not tasks:
            print("No tasks to mark.")
            return

        # Show tasks
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task.strip()}")

        # Get user choice
        num = int(input("Enter task number to mark as done: "))

        if num < 1 or num > len(tasks):
            print("Invalid task number.")
            return

        # Mark task as done
        if tasks[num - 1].startswith("[x]"):
            print("Task already marked as done.")
        else:
            tasks[num - 1] = tasks[num - 1].replace("[ ]", "[x]", 1)
            print("Task marked as done.")

        # Write back to file
        with open("Tasks.txt", "w") as f:
            f.writelines(tasks)

    except FileNotFoundError:
        print("No tasks file found.")
    except ValueError:
        print("Please enter a valid number.")
def delete():
  def delete():
    try:
        with open("Tasks.txt", "r") as f:
            tasks = f.readlines()

        if not tasks:
            print("No tasks to delete.")
            return

        # Show tasks
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task.strip()}")

        # Get user choice
        num = int(input("Enter task number to delete: "))

        if num < 1 or num > len(tasks):
            print("Invalid task number.")
            return

        # Delete task
        removed = tasks.pop(num - 1)
        print(f"Deleted: {removed.strip()}")

        # Write updated list back
        with open("Tasks.txt", "w") as f:
            f.writelines(tasks)

    except FileNotFoundError:
        print("No tasks file found.")
    except ValueError:
        print("Please enter a valid number.")
