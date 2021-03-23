import sqlite3
# make a connection to the db
conn = sqlite3.connect('my_db')
# create a cursor
curs = conn.cursor()
# an sql statement to READ from the db table
statement = '''SELECT * FROM zoo'''
curs.execute(statement)
rows = curs.fetchall()
print(rows)
# commit the changes
conn.commit()
conn.close() # close the connection and commit the changes