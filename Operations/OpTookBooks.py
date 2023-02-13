from Operations.OpBooks import *
from Operations.OpMember import *
class TookBook():
    def addTook(self):#Rezerve Ekleme Fonksiyonu
        bookID = int(input("Book ID:"))
        if(Book.checkBookStatusFromID(bookID)): #Kitabın Statusu rezerveye uygunluğu kontrol ediliyor.
            memberID = int(input("Member ID:"))
            if(Book.checkcMemberTookingFromID(memberID)): #Kiralacak Kullanıcının Kitap Alma sınırında olup olmadğı kontrol ediliyor.
                tookDate = input("Took Date:")
                datas = [memberID,bookID,tookDate]

                database.cur.execute("Insert into TookBooks(MemberID,BookID,TookDate) values(?,?,?)",datas)
                database.db.commit()

                print("Book was took")
            else:
                print("Maximum Book Number")
        else:
            print("Book is avaliable")

    def getMemberIDfromBookID(self,id):
        database.cur.execute("Select MemberID from TookBooks where BookID = {} ".format(id))
        data = database.cur.fetchone()
        return data[0]


