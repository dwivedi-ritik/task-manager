from sqlalchemy import Column, Integer, Text, String, DateTime, func
from sqlalchemy.orm import declarative_base

from database.db_handler import engine #Relative path 

Base = declarative_base()

class Task(Base):
    __tablename__ ="tasks"

    id = Column("id", Integer, primary_key=True, autoincrement="auto")
    task_name = Column("task_name", Text)
    status = Column("status", Text)

    def __init__(self, task_name:str, status:str):
        self.task_name = task_name
        self.status = status
    
    def get_id(self)-> int:
        return self.id

    def get_task_name(self)-> str:
        return self.task_name
    
    def get_status(self)-> str:
        return self.status

    def set_task_name(self, task: str):
        self.task_name = task
    
    def set_status(self, status: str):
        self.status = status

    def __repr__(self)->str:
        return f"TASK NAME: {self.task_name}\nSTATUS: {self.status}"

    @staticmethod
    def to_array(task):
        return [task.id, task.task_name, task.status]

Base.metadata.create_all(engine) #Creates table first