import sqlite3 as sql
from Operations.OpBooks import *
from Operations.OpMember import *
db = sql.connect("libraryDb.sqlite")
cur = db.cursor()

def addTook():#Rezerve Ekleme Fonksiyonu
    bookID = int(input("Book ID:"))
    if(checkBookStatusFromID(bookID)): #Kitabın Statusu rezerveye uygunluğu kontrol ediliyor.
        memberID = int(input("Member ID:"))
        if(checkcMemberTookingFromID(memberID)): #Kiralacak Kullanıcının Kitap Alma sınırında olup olmadğı kontrol ediliyor.
            tookDate = input("Took Date:")
            datas = [memberID,bookID,tookDate]

            cur.execute("Insert into TookBooks(MemberID,BookID,TookDate) values(?,?,?)",datas)
            db.commit()

            print("Book was took")
        else:
            print("Maximum Book Number")
    else:
        print("Book is avaliable")

def getMemberIDfromBookID(id):
    cur.execute("Select MemberID from TookBooks where BookID = {} ".format(id))
    data = cur.fetchone()
    return data[0]

