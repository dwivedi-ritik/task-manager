from tabulate import tabulate
import random
def print_table(table):
    print(tabulate(table , headers=["Task Id" , "Task" , "Deadline" , "Status"] , tablefmt="github"))

def get_random_id():
    return random.randrange(100 , 1000)