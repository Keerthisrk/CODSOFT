def show_menu():
    print("\n===== TO-DO LIST MENU =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Mark Task as Completed")
    print("5. Delete Task")
    print("6. Exit")


def add_task(todo_list):
    task = input("Enter the task: ")
    todo_list.append({"task": task, "status": "Pending"})
    print("✅ Task added successfully!")


def view_tasks(todo_list):
    if not todo_list:
        print("📭 No tasks available.")
        return

    print("\n📋 Your To-Do List:")
    for index, task in enumerate(todo_list, start=1):
        print(f"{index}. {task['task']} - {task['status']}")


def update_task(todo_list):
    view_tasks(todo_list)
    try:
        task_no = int(input("Enter task number to update: ")) - 1
        if 0 <= task_no < len(todo_list):
            new_task = input("Enter new task description: ")
            todo_list[task_no]["task"] = new_task
            print("✏️ Task updated successfully!")
        else:
            print("❌ Invalid task number.")
    except ValueError:
        print("❌ Please enter a valid number.")


def mark_completed(todo_list):
    view_tasks(todo_list)
    try:
        task_no = int(input("Enter task number to mark as completed: ")) - 1
        if 0 <= task_no < len(todo_list):
            todo_list[task_no]["status"] = "Completed"
            print("✔️ Task marked as completed!")
        else:
            print("❌ Invalid task number.")
    except ValueError:
        print("❌ Please enter a valid number.")


def delete_task(todo_list):
    view_tasks(todo_list)
    try:
        task_no = int(input("Enter task number to delete: ")) - 1
        if 0 <= task_no < len(todo_list):
            removed = todo_list.pop(task_no)
            print(f"🗑️ Task '{removed['task']}' deleted!")
        else:
            print("❌ Invalid task number.")
    except ValueError:
        print("❌ Please enter a valid number.")


def main():
    todo_list = []
    print("📝 Welcome to the To-Do List Application!")

    while True:
        show_menu()
        choice = input("Choose an option (1-6): ")

        if choice == "1":
            add_task(todo_list)
        elif choice == "2":
            view_tasks(todo_list)
        elif choice == "3":
            update_task(todo_list)
        elif choice == "4":
            mark_completed(todo_list)
        elif choice == "5":
            delete_task(todo_list)
        elif choice == "6":
            print("👋 Exiting To-Do List. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please select again.")


main()