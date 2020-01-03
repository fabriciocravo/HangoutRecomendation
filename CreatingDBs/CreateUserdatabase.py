import sqlite3

# Python code to demonstrate table creation and
# insertions with SQL

# importing module
import sqlite3

# connecting to the database
connection = sqlite3.connect("UserTable.db")

# cursor
crsr = connection.cursor()

# SQL command to create a table in the database
sql_command = """CREATE TABLE Users (  
user_id INTEGER PRIMARY KEY,  
uname VARCHAR(50),  
pword VARCHAR(50),  
latitude FLOAT(8),
longitude FLOAT(8)
);"""

# execute the statement
crsr.execute(sql_command)

# SQL command to insert the data in the table
sql_command = """INSERT INTO Users VALUES (0, "Fafa", "123", "123", "124");"""
crsr.execute(sql_command)

sql_command = """INSERT INTO Users VALUES (1, "Luke", "myDick", "123", "124");"""
crsr.execute(sql_command)

# To save the changes in the files. Never skip this.
# If we skip this, nothing will be saved in the database.
connection.commit()


sql_command = """
    SELECT *
    FROM Users
"""

crsr.execute(sql_command)
ans = crsr.fetchall()

for i in ans:
    print(i)

connection.close()
