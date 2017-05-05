import mysql.connector
cnx = mysql.connector.connect(user='iorilan', password='lanliang',
                              host='iorilan.mysql.pythonanywhere-services.com',
                              database='iorilan$default')

cursor = cnx.cursor()

query = ("SELECT FirstName,LastName FROM Persons ")

cursor.execute(query)

for (FirstName, LastName) in cursor:
  print("{}, {} ".format(
    FirstName, LastName))

cursor.close()
cnx.close()