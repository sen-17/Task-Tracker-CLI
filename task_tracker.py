print("""
Welcome to the Task Tracker CLI!
This tool helps you manage your tasks efficiently.
You can add tasks, view your task list, and mark tasks as completed.
Please follow the prompts to get started.""")

def task_to_json(task):
    import json
    with open('tasks.json', 'w') as file:
        json.dump(task, file, indent=4)

def main():
    tasks = []

    while True:
        print("\n Task Tracker Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete task")
        print("5. Exit")

        choice = input("Please enter your choice (1-5): ")

        if choice == '1':
            task_name = input("Enter the task name: ")
            tasks.append({"name": task_name, "completed": False})
            task_to_json(tasks)
            print(f"Task '{task_name}' added successfully.")

        elif choice == '2':
            if not tasks:
                print("No tasks available.")
            else:
                print("Current Tasks:")
                for index, task in enumerate(tasks, start=1):
                    status = "✔️" if task["completed"] else "❌"
                    print(f"{index}. {task['name']} [{status}]")

        elif choice == '3':
            user_choice = input("Which task do you want to mark as completed? (Enter task number): ")
            try:
                task_index = int(user_choice) - 1
                if 0 <= task_index < len(tasks):
                    tasks[task_index]["completed"] = True
                    print(f"Task '{tasks[task_index]['name']}' marked as completed.")
                    task_to_json(tasks)
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")
        
        elif choice == '4':
            user_choice = input("Which task do you want to delete? (Enter task number): ")
            try:
                task_index = int(user_choice) - 1
                if 0 <= task_index < len(tasks):
                    deleted_task = tasks.pop(task_index)
                    print(f"Task '{deleted_task['name']}' deleted.")
                    task_to_json(tasks)
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

        elif choice == '5':
            print("Exiting Task Tracker. Goodbye!")
            break   

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()

        