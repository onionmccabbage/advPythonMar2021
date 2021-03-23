import sqlite3 # sqlite3 is the database that comes with Python

# make a connection to the db
conn = sqlite3.connect('my_db') # creates the db if it does not exist
# create a cursor
curs = conn.cursor() # a cursor allows us to work with the db
# excecute a statement
statement = '''CREATE TABLE zoo 
               (creature VARCHAR(20) PRIMARY KEY,
                count INT,
                cost FLOAT)'''
curs.execute(statement) # apply the SQL statement to the db

# commit the changes
conn.commit()
# always remember to close the connection
conn.close() # close the connection