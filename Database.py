import sqlite3 as sql

class Database():
    db = sql.connect("libraryDb.sqlite")
    cur = db.cursor()

