import mysql.connector

dataBase = mysql.connector.connect(
   host = 'localhost',
   user = 'root',
   password = 'M@trix.1991'
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE codepedia")

print('all done ...')