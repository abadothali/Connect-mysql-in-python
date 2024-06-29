# CONNECT MYSQL IN PYTHON---------------
import mysql.connector as mycon
db=mycon.connect(
  host="localhost",
  user="root",
  password="abadothali",
  database="nit"
)


# CEATE NIT DATABASE-------------------------------------------
# dbCursor=db.cursor()
# dbCursor.execute("CREATE DATABASE nit")
# print("databases is creating.........")


# CREATE STUDENT TABLE IN NIT DATABASE--------------------------
# dbCursor=db.cursor()
# dbCursor.execute("CREATE TABLE student(id int, name varchar(50), age int not null)")
# print("creating table..............")


# CHECK HOW MANY TABLES HAVE IN NIT DATABASE----------------
# dbCursor=db.cursor()
# dbCursor.execute("SHOW TABLES")
# print("tables are.........")
# for i in dbCursor:
#   print(i)


# INSERT DATA IN STUDENT TABLE----------------------
# dbCursor=db.cursor()
# insert="insert into student(id,name,age) values(%s,%s,%s)"
# insert_data=[(1,"monirul",22),(2,"rupsa",20),(3,"rahul",21)]
# dbCursor.executemany(insert,insert_data)
# db.commit()
# print(dbCursor.rowcount,"record has insert.........")


# SHOW ALL DATA FROM STUDENT TABLE----------------
# dbCursor=db.cursor()
# dbCursor.execute("SELECT * FROM STUDENT;")
# print("data's are.........")
# for i in dbCursor:
#   print(i)
# print(dbCursor.rowcount,"rows have in this table......")


# UPDATE DATA........................
# dbCursor=db.cursor()
# update="update student set id=%s where name=%s"
# set_value=(7,'rupsa')
# dbCursor.execute(update,set_value)
# db.commit()
# print(dbCursor.rowcount,"Updated.......")


# DELETE DATABASES---------------------
# dbCursor=db.cursor()
# dbCursor.execute("DROP DATABASE IF EXISTS fk;")
# print("deleted database............")


# SHOW ALL DATABASE IN DB---------------------------
dbCursor=db.cursor()
dbCursor.execute("SHOW DATABASES;")
print("All database............")
for i in dbCursor:
  print(i)
print(dbCursor.rowcount,"databases is present.............")