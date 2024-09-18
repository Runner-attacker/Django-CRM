import mysql.connector

dataBase = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="password123",
)
# prepare a cursor object

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE sahildb")
print("Database Connected Sucessfully")
