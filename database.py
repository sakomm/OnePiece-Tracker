import sqlite3 as dbc
import os 

db = "shitdb.db"
sql = "schema.sql"
global schema

def check_db():
    return os.path.exists(db)    

if not check_db():
    raise Exception("DATABASE DOES NOT EXIST -- PLEASE CHECK PATH")
    
with open(sql, 'r') as rf:
    # Read the schema from the file
    schema = rf.read()

with dbc.connect(db) as conn:
    print('Created the connection!')
    # Execute the SQL query to create the table
    conn.executescript(schema)