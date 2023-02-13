from Operations.OpBooks import *
class Received:
    def addReceived(self):
        bookID = int(input("Book ID:"))
        if (Book.checkBookStatusFromID(bookID)): #Kitabın Statusu rezerve edilmeye uygunluğu kontrol ediliyor.
            memberID = int(input("Member ID:"))
            receivedDate = input("Received Date:")
            datas = [memberID,bookID,receivedDate]

            database.cur.execute("Insert into ReceivedBooks(MemberID,BookID,TookDate) values(?,?,?)",datas)
            database.db.commit()
            print("Book reserved.")
        else:
            print("Book is not avaliable.")


