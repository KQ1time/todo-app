# version 0.1.1

from task_manager import TaskManager

# Program for creating tasks


def main():
    """
    Main function of program. It is GUI and it uses other functions.

    Args:
        None

    Returns:
        None
    """

    manager = TaskManager("tasks.json")

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

        tasks = manager.tasks_read()

        if choice == 1:
            task = input("Your task \n")
            task_id = manager.create_id(tasks)

            manager.create(tasks, task_id, task)
        
        elif choice == 2:
            try:
                task_id = input("ID of task \n")
                manager.delete(tasks, task_id)

            except KeyError:
                print("Please, enter valid ID")

        elif choice == 3:
            print("Tasks:")

            for key, value in tasks.items():
                print(key, value)

        elif choice == 0:
            break

main()