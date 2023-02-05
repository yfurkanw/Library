import sqlite3 as sql
from Operations.OpBooks import *

db = sql.connect("libraryDb.sqlite")
cur = db.cursor()

def addReceived():
    bookID = int(input("Book ID:"))
    if (checkBookStatusFromID(bookID)): #Kitabın Statusu rezerve edilmeye uygunluğu kontrol ediliyor.
        memberID = int(input("Member ID:"))
        receivedDate = input("Received Date:")
        datas = [memberID,bookID,receivedDate]

        cur.execute("Insert into ReceivedBooks(MemberID,BookID,TookDate) values(?,?,?)",datas)
        db.commit()
        print("Book reserved.")
    else:
        print("Book is not avaliable.")


