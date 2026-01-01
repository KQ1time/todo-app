import json

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