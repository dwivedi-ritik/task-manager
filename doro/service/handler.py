from sqlalchemy import select
from models.model import Task
from constants import Status

class Service: 
    def __init__(self, session):
        self.session = session

    def get_all_task(self):
        modelRows = self.session.query(Task).all()
        allRows = []
        for row in modelRows:
            allRows.append([ row.get_id(), row.get_task_name(), row.get_status()])
        return allRows

    def add_task(self, task):
        newRow = self.session.add(task)
        self.session.commit()
        return newRow
    
    def set_task_done_by_id(self, id):
        updateTask = self.session.query(Task).get(id)
        updateTask.set_status(Status.DONE)
        self.add_task(updateTask)
        self.session.commit()
        return updateTask

    def get_task_by_id(self, id):
        return self.session.query(Task).get(id)

    def get_all_pending_task(self):
        return self.session.query(Task).filter(Task.status == Status.PENDING)
    
    def get_all_done_task(self):
        return self.session.query(Task).filter(Task.status == Status.DONE)


    @staticmethod
    def get_2d_array_of_query(task):
        pass

    
