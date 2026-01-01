# version 0.1.1

import json

# Program for creating tasks

class TaskManager:

    def __init__(self, filename):
        self.filename = filename


    def create(self, tasks, task_id, task):
        with open(self.filename, "w") as f:
            tasks[task_id] = task
            json.dump(tasks, f, indent=4)

    
    def delete(self, tasks, task_id):
        del tasks[task_id]

        with open(self.filename, "w") as file:
            json.dump(tasks, file)
    
    def create_id(self, tasks):
        count = 1

        while str(count) in tasks:
            count += 1

        return str(count)

    
    def tasks_read(self):
        try:
            with open(self.filename, "r") as file:
                tasks = json.load(file)
        
        except (json.JSONDecodeError, FileNotFoundError):
            with open(self.filename, "w") as file:
                tasks = {}
                json.dump(tasks, file)

        return tasks


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
