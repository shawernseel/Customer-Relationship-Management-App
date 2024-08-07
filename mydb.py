import os
from dotenv import load_dotenv
import mysql.connector
load_dotenv()

dataBase = mysql.connector.connect(
    host ='localhost',
    user = os.getenv("DB_USER"),
    passwd = os.getenv("DB_PASSWORD"),
)

# prepare a cursor object
cursorObject = dataBase.cursor()

# Create a database
cursorObject.execute("CREATE DATABASE crmDB")

print("All Done!")