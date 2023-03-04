from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from constants import sqlite_path


engine = create_engine(sqlite_path , echo=False)
Session = sessionmaker(bind=engine)






