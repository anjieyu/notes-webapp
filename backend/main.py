import sqlite3

def connect_db():
    connection = sqlite3.connect("notes.db")
    connection.row_factory = sqlite3.Row
    return connection