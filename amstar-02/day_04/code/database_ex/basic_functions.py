import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root"
)

mycursor = mydb.cursor()


print('Database creation')
#mycursor.execute("CREATE DATABASE mydatabase")



print('\n\nShowing databases')
#mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)


