import mysql.connector
import pandas as pd


mydb = mysql.connector.connect(
    host='localhost',
    user = 'root',
    password='4Aepitie44!',
    database = "testdb"
)
print(mydb)
df =pd.read_sql_query("SELECT * FROM students", mydb)
print(df)

mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM students")
myresult = mycursor.fetchall()
myresult = mycursor.fetchone()



# while myresult != None:
#
#     print(myresult)
#
# for entry in myresult:
#      print (entry)
#
sqlformula = "SELECT * FROM students WHERE age > %s"
mycursor.execute(sqlformula, (30,))
myresult= mycursor.fetchall()
for res in myresult:
    print(res)

# mycursor.execute("CREATE DATABASE testdb")
# mycursor.execute("SHOW DATABASE")
# student1=('Rob', 25)
# student2=[('Kit', 76),("Kolya",19), ('Roman',55)]
# name = 'Mary'
# age= 25

# mycursor.execute('CREATE TABLE students (name VARCHAR(45), age INTEGER(10))')
# mycursor.execute('INSERT INTO students(name,age) VALUES("'+ name + '", '+ str(age) +')')
# sqlquery=('INSERT INTO students(name,age) VALUES(%s, %s)')
# mycursor.execute(sqlquery, student1)
# mycursor.executemany(sqlquery, student2)
#
# mydb.commit()
# for table in mycursor:
#     print(table[0])