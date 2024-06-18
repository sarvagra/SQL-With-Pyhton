# to fetch data from table through pyhthon.
import logging
import os
from dotenv import load_dotenv
load_dotenv()
import mysql.connector

logging.basicConfig(filename="04a_logging.log",level=logging.DEBUG, format='%(asctime)s%(message)s')
logging.info("connecting with database")
mydb = mysql.connector.connect(
    host="localhost",
    user = "root",
    password=os.getenv('pass')
)
mycursor=mydb.cursor()
#to fetch all columns:
logging.info("fetching all columns")
mycursor.execute("select * from sarvagra.table_one")

for i in mycursor.fetchall():
    logging.info(i)

#to fetch selected columns
logging.info("fetching selected columns")
mycursor.execute("select c1 , c4 from sarvagra2.table_two")

for i in mycursor.fetchall():
    logging.info(i)
mydb.close()