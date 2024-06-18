#how to connect with sql through python.
import logging
import os
from dotenv import load_dotenv
load_dotenv()
import mysql.connector

logging.basicConfig(filename="00a_logging.log",level=logging.DEBUG,format='%(asctime)s %(message)s')
logging.info("Connecting python with SQL")
mydb = mysql.connector.connect(
    host="localhost",
    user = "root",
    password=os.getenv('pass')
)
logging.info("printing all databases")
logging.info(mydb)
mycursor=mydb.cursor()
mycursor.execute("show databases")
for x in mycursor:
    logging.info(x)