import sqlite3
# make a connection to the db
conn = sqlite3.connect('my_db')
# create a cursor
curs = conn.cursor()
# an sql statement to WRITE to the db table
statement = '''INSERT INTO zoo VALUES("duck", 5, 0.30)'''
curs.execute(statement)
statement = '''INSERT INTO zoo VALUES("bear", 2, 1500.09)'''
curs.execute(statement)
statement = '''INSERT INTO zoo VALUES("panda", 1, 10000.00)'''
curs.execute(statement)
# commit the changes
conn.commit()
conn.close() # close the connection 