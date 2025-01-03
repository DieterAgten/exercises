from datetime import date

class Taks:
    def __init__(self, description, due_date):
        self.__description = description
        self.finished = False
        self.__due_date= due_date

    @property
    def description(self):
        return self.__description
    
    @property
    def due_date(self):
        return self.__due_date
    
class Takslist:
    def __init__(self):
        self.tasks = []

    def __len__(self):
        return len(self.__tasks)
    
    def add_task(self, task):
        if task.due_date < date.today():
            raise RuntimeError()
        self.__tasks.append(task)

    @property
    def finished_tasks(self):
        return [task for task in self.__tasks if task.finished]
    
    @property
    def due_tasks(self):
        return [task for task in self.__tasks if not task.finished]
    
    @property
    def overdue_tasks(self):
        return [task for task in self.__tasks if task.finished and task.due_date < date.today()]