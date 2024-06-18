# how to make a table with python.
import logging
import os
from dotenv import load_dotenv
load_dotenv()
import mysql.connector

logging.basicConfig(filename="02a_logging.log",level= logging.DEBUG,format='%(asctime)s %(message)s')
logging.info("connecting with databse")
mydb = mysql.connector.connect(
    host="localhost",
    user = "root",
    password=os.getenv('pass')
)
logging.info("creating table_two")
mycursor=mydb.cursor()
mycursor.execute("CREATE TABLE if not exists sarvagra2.table_two(c1 INT, c2 VARCHAR(50),c3 FLOAT, c4 INT, c5 VARCHAR(30))")
mydb.close()