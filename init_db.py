import sqlite3

connection = sqlite3.connect('database.db')

# Only run if the 'skills' table does not exist, since it will drop the table
with open('schema.sql') as f:
    connection.executescript(f.read())