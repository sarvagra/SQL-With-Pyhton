# how to make a database with python.
import logging
import os
from dotenv import load_dotenv
load_dotenv()
import mysql.connector

logging.basicConfig(filename="01a_logging.log",level= logging.DEBUG,format='%(asctime)s %(message)s')
logging.info("connecting to SQL")
mydb = mysql.connector.connect(
    host="localhost",
    user = "root",
    password=os.getenv('pass')
)
logging.info("creating database sarvagra2")
mycursor=mydb.cursor()
mycursor.execute("CREATE DATABASE if not exists sarvagra2")
mydb.close()