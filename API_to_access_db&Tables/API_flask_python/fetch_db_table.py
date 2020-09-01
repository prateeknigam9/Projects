import mysql.connector

db = mysql.connector.connect(
    host = 'localhost',
    user ='root',
    passwd = 'Mumbai@143'
) 

db_to_fetch = "db2"
table_to_fetch = "DSA_db2"
mycursor = db.cursor()

mycursor.execute("USE "+str(db_to_fetch))
mycursor.execute("SELECT * FROM "+ str(table_to_fetch))
result = mycursor.fetchall()

for row in result:
    print(row)