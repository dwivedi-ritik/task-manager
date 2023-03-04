import argparse

from database import Session
from service import Service
from models import Task
from utils import print_table
from constants import Status

parser = argparse.ArgumentParser(description="Command line task tracker" , epilog="")
parser.add_argument("--mark" , "-m" , help="Mark you task complete , pass task id" , dest="mark" , metavar='')
parser.add_argument("--delete" , "-d" , help="Delete your tasks , pass task id" , dest="delete" , metavar='')
parser.add_argument("--create-task" , "-a" , help="Add some other task" , action='store_true' , dest='task')
parser.add_argument("--all" , "-g" , help="Get all of your tasks" , action='store_true' , dest='all_tasks')
parser.add_argument("--pending" , "-p" , help="Get list of completed tasks" , action='store_true' , dest="com")
parser.add_argument("--complete" , "-c" , help="Get list of incomplete tasks" , action='store_true' , dest="icom")
args = parser.parse_args()

session= Session()
service = Service(session=session)


if args.task:
    try:
        task = input("What is the Task :> ")
        newTask = Task(task_name=task , status=Status.PENDING)
        service.add_task(newTask)
    except Exception:
        raise Exception

if args.all_tasks:
    allRows = service.get_all_task(Task)
    print_table(allRows)
    
# print_table(service.get_task_by_id(2))

print_table(service.get_all_task())

# print_table(service.mark_complete(1))