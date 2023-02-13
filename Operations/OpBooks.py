from Database import Database

database = Database()

class Book:
    def addBook(self): #Kitap Eklem fonksiyonumuz.
        name = input("Category Name:")
        Author = input("Author Name:")
        isbn_No = int(input("ISBN No:"))
        Address = input("Adress:")
        PublicationDate = input("Publication Date:")
        Status = "Free"

        Category_ID = int(input("Category ID:"))
        dataAddBook = [name, Author, isbn_No, Address, PublicationDate,Status,Category_ID] #Alınan verileri bir listede tuttuk.

        database.cur.execute("Insert into Books(Name,Author,ISBN,Address,PublicationDate,Status,Category_ID) "
                    "values(?,?,?,?,?,?,?)",dataAddBook) #Sorgumuzu veritabanına gönderdik.
        database.db.commit() #Veritabanındaki değişiklikleri kaydettik.

        print("Book Added")

    def getBooksAll(self):#Tüm Kitapları getirme fonksiyonumuz
        database.cur.execute("Select * from Books") #Tüm kitapları getiricek sorgumuzu veritabanımıza gönderdik.
        datas = database.cur.fetchall() #Veritabanından gelen verileri aldık.
        return datas

    def getBooksFromName(self,text):#İsme göre kitap getirme fonksiyonumuz
        database.cur.execute("Select * from Books where Name Like '%{}%' ".format(text)) #Belirtilen kitap adını içeren kitapları listeleyecek sorgumuzu gönderdik.
        datas = database.cur.fetchall()#Veritabanından gelen verileri aldık.
        return datas

    def getBooksFromAuthor(self,text):#Yazara göre kitap getirme fonksiyonumuz
        database.cur.execute("Select * from Books where Author Like '%{}%' ".format(text)) #Belirtilen parametreye göre arama yaptık.
        datas = database.cur.fetchall()#Veritabanından gelen verileri aldık.
        return datas

    def getBooksFromStatus(self,text):#Status'e göre kitap getirme fonksiyonumuz
        database.cur.execute("Select * from Books where Status Like '%{}%' ".format(text))#Belirtilen parametreye göre arama yaptık.
        datas = database.cur.fetchall()#Veritabanından gelen verileri aldık.
        return datas

    def getBooksFromBookID(self,id):#ID'ye göre kitap getirme fonksiyonumuz
        database.cur.execute("Select * from Books where BookID = ?  ",(id,))#Belirtilen parametreye göre arama yaptık.
        data = database.cur.fetchone()#Veritabanından gelen veriyi aldık.
        return data

    def getBooksFromCategoryID(self,id):#Kategori ID'ye göre kitap getirme fonksiyonumuz
        database.cur.execute("Select * from Books where BookID = ?  ",(id,))#Belirtilen parametreye göre arama yaptık.
        datas = database.cur.fetchall()#Veritabanından gelen verileri aldık.
        return datas

    def deleteBookFromID(self,id):#Kitap Silme Fonksiyonumuz
        print("Silinecek Kitap:",end=" ")
        print(getBooksFromBookID(id)) #Belirtilen ID'ye göre işlem yapılacak veriyi getirdik.
        database.cur.execute("Delete Books where BookID = {}".format(id))#Silme işlemi yapıldı
        database.db.commit()
        print("Book deleted")

    def updateBookNameFromID(self,id):#Kitap Adı Güncelleme Fonksiyonumuz
        print("Book to be updated:", end=" ")
        print(self.getBooksFromBookID(id))#Belirtilen ID'ye göre işlem yapılacak veriyi getirdik.
        name = input("Update Book Name:")
        database.cur.execute("Update Books set Name='{}' where BookID = {}".format(name, id))#Güncelleme işlemi yapıldı
        database.db.commit()
        print("Book updated")

    def updateBookAuthorFromID(self,id):#Kitap Yazarı Güncelleme Fonksiyonumuz
        print("Update Book Name:", end=" ")
        print(self.getBooksFromBookID(id))#Belirtilen ID'ye göre işlem yapılacak veriyi getirdik.
        author = input("Update Book Author:")
        database.cur.execute("Update Books set Author='{}' where BookID = {}".format(author, id))#Güncelleme işlemi yapıldı
        database.db.commit()
        print("Book Updated")

    def updateBookIsbnFromID(self,id):#Kitap ISBN Numarası Güncelleme Fonksiyonumuz
        print("Update Book Name:", end=" ")
        print(self.getBooksFromBookID(id))#Belirtilen ID'ye göre işlem yapılacak veriyi getirdik.
        isbn = int(input("Update Book ISBN:"))
        database.cur.execute("Update Books set ISBN={} where BookID = {}".format(isbn, id))#Güncelleme işlemi yapıldı
        database.db.commit()
        print("Book Updated")

    def checkBookStatusFromID(self,id):#Kitap Statusu Kontrol Fonksiyonumuz
        database.cur.execute("Select Status from Books where BookID = ?  ", (id,))#Belirtilen parametreye göre arama yaptık.
        data = database.cur.fetchone()
        print(data)
        if(data[0] == "Free"):#Eğer Status uygunsa True,değilse False gönderdik.
            return True
        else:
            return False

