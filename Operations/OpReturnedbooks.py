from Operations.OpTookBooks import *
class Returned:
    def addReturned(self):
        bookID = int(input("Book ID:"))
        if (Book.checkBookStatusFromID(bookID) == False):#Kitabın Statusu şuan kiralamada olup olmadığı kontrol ediliyor.
            memberID = int(MemberClass.getMemberIDfromBookID(bookID))
            returnedDate = input("Returned Date:")
            datas = [memberID,bookID,returnedDate]
            database.db.execute("Insert into ReturnedBooks(MemberID,BookID,ReturnedDate) values(?,?,?)",datas)
            database.db.commit()
            print("Book unreserved")
        else:
            print("Book avaliable.")

