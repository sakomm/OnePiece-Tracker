import sqlite3 as db 
import os 

db = "shitdb.db"
sql = "schema.sql"

def check_db():
    return os.path.exists(db)    

if not check_db():
    raise Exception("DATABASE DOES NOT EXIST -- PLEASE CHECK PATH")
    
con = db.connect(db)


