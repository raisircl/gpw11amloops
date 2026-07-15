import sqlite3

# create the connection object 
#connect function check the db file if it is not present then 
# it will create a new db file
conn=sqlite3.connect("payroll.db")

# create the cursor object
# it is reponsible for Create, Read, Update and Delete operations (CRUD)
cursor=conn.cursor()

print("Database created and Successfully Connected to SQLite")


# never forget to close the connection
conn.close()

