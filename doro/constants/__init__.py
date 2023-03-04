class Status:
    PENDING:str="Pending"
    DONE:str="Done"

sqlite_path = "sqlite:///mydb.db" 

__all__ = ["sqlite_path" , 'Status']