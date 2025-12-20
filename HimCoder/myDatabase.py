import mysql.connector

mydb = mysql.connector.connection(
    host="localhost",
    user="admin",
    password="",
    database="Company"
)

sql = "create table employee(eno int primary key, ename varchar(50), gender varchar(1))"

mycursor = mydb.cursor()

mycursor.execute(sql)

mycursor.close()
mydb.close()
