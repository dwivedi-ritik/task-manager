#!/usr/bin/python

import argparse
import psycopg2
import sys
import time
import os
from dotenv import load_dotenv

load_dotenv()

conn = psycopg2.connect(
    database= os.environ.get("database"),
    user = os.environ.get("username") ,
    host = 'localhost'
)
db = conn.cursor()

def fetch_all():
    db.execute('SELECT * FROM Tasks')
    res = db.fetchall()
    db.close()
    conn.close()
    return res 

def fetch_completed():
    db.execute("SELECT * FROM Tasks WHERE STATUS='completed' ")
    res = db.fetchall()
    db.close()
    conn.close()
    return res

def create_task(task , deadline):
    unix_time = int(time.time())
    params = (unix_time , task , deadline ,  'incomplete')
    command = "INSERT INTO Tasks (key , task , deadline , status) VALUES(%s , %s , %s , %s)" 
    db.execute(command , params)
    conn.commit()
    db.close()
    conn.close()

def fetch_incomplete():
    db.execute("SELECT * FROM Tasks WHERE STATUS='incomplete' ")
    res = db.fetchall()
    db.close()
    conn.close()
    return res

def delete_record(_id):
    command = "DELETE FROM Tasks WHERE key = %s"
    params = (_id , )
    db.execute(command , params)
    conn.commit()
    db.close()
    conn.close()

def mark_complete(_id):
    command = "UPDATE Tasks SET status = %s WHERE key = %s"
    params = ('completed' , _id)
    db.execute(command , params)
    conn.commit() 
    print("New Row Count is {}".format(db.rowcount))   

    db.close()
    conn.close()
