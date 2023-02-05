import sqlite3 as sql
from Operations.OpBooks import *
from Operations.OpTookBooks import *
db = sql.connect("libraryDb.sqlite")
cur = db.cursor()

def addReturned():
    bookID = int(input("Book ID:"))
    if (checkBookStatusFromID(bookID) == False):#Kitabın Statusu şuan kiralamada olup olmadığı kontrol ediliyor.
        memberID = int(getMemberIDfromBookID(bookID))
        returnedDate = input("Returned Date:")
        datas = [memberID,bookID,returnedDate]
        cur.execute("Insert into ReturnedBooks(MemberID,BookID,ReturnedDate) values(?,?,?)",datas)
        db.commit()
        print("Book unreserved")
    else:
        print("Book avaliable.")

