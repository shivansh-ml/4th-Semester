class Task:
    def __init__(self, description):
        self.description = description
    
    def __str__(self):
        return self.description

class TodoList:
    def __init__(self):
        self.tasks = []
    
    def add_task(self, task):
        self.tasks.append(task)
    
    def remove_task(self, task_desc):
        self.tasks = [task for task in self.tasks if task.description != task_desc]
    
    def display_tasks(self):
        for task in self.tasks:
            print(task)

my_list = TodoList()
my_list.add_task(Task("Complete assignment"))
my_list.add_task(Task("Buy groceries"))
my_list.display_tasks()
