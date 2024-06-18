# how to insert data in table with python.
import logging
import os
from dotenv import load_dotenv
load_dotenv()
import mysql.connector

logging.basicConfig(filename="03a_logging.log",level= logging.DEBUG,format='%(asctime)s %(message)s')
logging.info("connecting with database")
mydb = mysql.connector.connect(
    host="localhost",
    user = "root",
    password=os.getenv('pass')
)
mycursor=mydb.cursor()

logging.info("inserting data into table one from sarvagra database.")
mycursor.execute("insert into sarvagra.table_one values(123, 'sarvagra', 23.456, 911, 'singh' )")
logging.info("inserting data into table two from sarvagra2 database.")
mycursor.execute("insert into sarvagra2.table_two values(733, 'sarv', 34.096, 37, 'S' )")
mycursor.execute("insert into sarvagra2.table_two values(733, 'sarv', 34.096, 37, 'S' )")
mycursor.execute("insert into sarvagra2.table_two values(733, 'sarv', 34.096, 37, 'S' )")
mycursor.execute("insert into sarvagra2.table_two values(733, 'sarv', 34.096, 37, 'S' )")
mycursor.execute("insert into sarvagra2.table_two values(733, 'sarv', 34.096, 37, 'S' )")
mydb.commit()
mydb.close()

