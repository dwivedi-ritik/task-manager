#!/usr/bin/python

import psycopg2
from psycopg2.errors import DuplicateTable
import os
from dotenv import load_dotenv

load_dotenv()

conn = psycopg2.connect(
    database= os.environ.get("database"),
    user = os.environ.get("username") ,
    host = 'localhost'
)
db = conn.cursor()

def if_not_then_create():
    try:
        command = "CREATE TABLE Tasks( key INTEGER PRIMARY KEY ,\
            task VARCHAR(1000) , \
            deadline VARCHAR(50) , \
            status VARCHAR(20) )"
        db.execute(command)
    except DuplicateTable:
        print("Table Already Exists")

if_not_then_create()
conn.commit()
db.close()
conn.close()