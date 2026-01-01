# version 1.0

import json

# Program for creating tasks

def main():
    """
    Main function of program. It is GUI and it uses other functions.

    Args:
        None

    Returns:
        None
    """
    while True:
        print(
            "\n"
            "1. Create task \n"
            "2. Delete task \n"
            "3. Show all tasks \n"
            "0. Exit"
        )

        try:
            choice = int(input("\n"))
        except ValueError:
            print("Please, enter 1, 2, 3 or 0")
            continue

        print("")

        if choice == 1:
            tasks = tasks_read()

            task = input("Your task \n")

            task_id = create_id(tasks)
            create(tasks, task_id, task)

        elif choice == 2:
            tasks = tasks_read()

            try:
                task_id = input("ID of task \n")
                delete(tasks, task_id)
            except KeyError:
                print("Please, enter valid ID")

        elif choice == 3:
            tasks = tasks_read()
            print("Tasks:")

            for key, value in tasks.items():
                print(key, value)

        elif choice == 0:
            break


def create(tasks, task_id, task):
    """
    Create task by ID and user's description.
    
    Args:
        tasks (dict): tasks (dict): Dictionary which have all tasks and their ID.
        task_id (str): ID of the task.
        task (str): User's description of task.

    Returns:
        None
    """
    with open("tasks.json", "w") as f:
        tasks[task_id] = task
        json.dump(tasks, f, indent=4)


def create_id(tasks):
    """
    Create id for task.
    
    Args:
        tasks (dict): Dictionary which have all tasks and their ID.
    
    Returns:
        count (str): ID of the task
    """
    count = 1

    while str(count) in tasks:
        count += 1
    
    return str(count)


def delete(tasks, task_id):
    """
    Delete task by ID.

    Args:
        tasks (dict): Dictionary which have all tasks and their ID.
        task_id (str): ID of the task.

    Returns:
        None
    """
    del tasks[task_id]

    with open("tasks.json", "w") as file:
        json.dump(tasks, file)


def tasks_read():
    """
    Read tasks from tasks.json and return them.

    Args:
        None
    
    Returns:
        tasks (dict): Dictionary which have all tasks and their ID.
    """
    try:
        with open("tasks.json", "r") as f:
            tasks = json.load(f)

    except (json.JSONDecodeError, FileNotFoundError):
        with open("tasks.json", "w") as f:
            tasks = {}
            json.dump(tasks, f)

    return tasks
        

main()
