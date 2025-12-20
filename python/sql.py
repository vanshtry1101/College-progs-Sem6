import mysql.connector as ms

#1.connect database
con=ms.connect(host="localhost",user='Rinki',password="1234",database="mca")
print(con)

#2.cursor - class to execute all queries 
cur=con.cursor()

#3.execute() method to execute all quires

cur.execute("create table student(sno int primary key, sname varchar(20))")
print("Created")

#4.close
cur.close()
con.close
