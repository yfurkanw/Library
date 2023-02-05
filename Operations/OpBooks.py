import sqlite3 as sql
db = sql.connect("libraryDb.sqlite") #Veritabanımıza bağlandık.
cur = db.cursor() #İşlemler için cursor oluşturduk.

def addBook(): #Kitap Eklem fonksiyonumuz.
    name = input("Category Name:")
    Author = input("Author Name:")
    isbn_No = int(input("ISBN No:"))
    Address = input("Adress:")
    PublicationDate = input("Publication Date:")
    Status = "Free"

    Category_ID = int(input("Category ID:"))
    dataAddBook = [name, Author, isbn_No, Address, PublicationDate,Status,Category_ID] #Alınan verileri bir listede tuttuk.

    cur.execute("Insert into Books(Name,Author,ISBN,Address,PublicationDate,Status,Category_ID) "
                "values(?,?,?,?,?,?,?)",dataAddBook) #Sorgumuzu veritabanına gönderdik.
    db.commit() #Veritabanındaki değişiklikleri kaydettik.

    print("Book Added")

def getBooksAll():#Tüm Kitapları getirme fonksiyonumuz
    cur.execute("Select * from Books") #Tüm kitapları getiricek sorgumuzu veritabanımıza gönderdik.
    datas = cur.fetchall() #Veritabanından gelen verileri aldık.
    return datas

def getBooksFromName(text):#İsme göre kitap getirme fonksiyonumuz
    cur.execute("Select * from Books where Name Like '%{}%' ".format(text)) #Belirtilen kitap adını içeren kitapları listeleyecek sorgumuzu gönderdik.
    datas = cur.fetchall()#Veritabanından gelen verileri aldık.
    return datas

def getBooksFromAuthor(text):#Yazara göre kitap getirme fonksiyonumuz
    cur.execute("Select * from Books where Author Like '%{}%' ".format(text)) #Belirtilen parametreye göre arama yaptık.
    datas = cur.fetchall()#Veritabanından gelen verileri aldık.
    return datas

def getBooksFromStatus(text):#Status'e göre kitap getirme fonksiyonumuz
    cur.execute("Select * from Books where Status Like '%{}%' ".format(text))#Belirtilen parametreye göre arama yaptık.
    datas = cur.fetchall()#Veritabanından gelen verileri aldık.
    return datas

def getBooksFromBookID(id):#ID'ye göre kitap getirme fonksiyonumuz
    cur.execute("Select * from Books where BookID = ?  ",(id,))#Belirtilen parametreye göre arama yaptık.
    data = cur.fetchone()#Veritabanından gelen veriyi aldık.
    return data

def getBooksFromCategoryID(id):#Kategori ID'ye göre kitap getirme fonksiyonumuz
    cur.execute("Select * from Books where BookID = ?  ",(id,))#Belirtilen parametreye göre arama yaptık.
    datas = cur.fetchall()#Veritabanından gelen verileri aldık.
    return datas

def deleteBookFromID(id):#Kitap Silme Fonksiyonumuz
    print("Silinecek Kitap:",end=" ")
    print(getBooksFromBookID(id))#Belirtilen ID'ye göre işlem yapılacak veriyi getirdik.
    cur.execute("Delete Books where BookID = {}".format(id))#Silme işlemi yapıldı
    db.commit()
    print("Book deleted")

def updateBookNameFromID(id):#Kitap Adı Güncelleme Fonksiyonumuz
    print("Book to be updated:", end=" ")
    print(getBooksFromBookID(id))#Belirtilen ID'ye göre işlem yapılacak veriyi getirdik.
    name = input("Update Book Name:")
    cur.execute("Update Books set Name='{}' where BookID = {}".format(name, id))#Güncelleme işlemi yapıldı
    db.commit()
    print("Book updated")

def updateBookAuthorFromID(id):#Kitap Yazarı Güncelleme Fonksiyonumuz
    print("Update Book Name:", end=" ")
    print(getBooksFromBookID(id))#Belirtilen ID'ye göre işlem yapılacak veriyi getirdik.
    author = input("Update Book Author:")
    cur.execute("Update Books set Author='{}' where BookID = {}".format(author, id))#Güncelleme işlemi yapıldı
    db.commit()
    print("Book Updated")

def updateBookIsbnFromID(id):#Kitap ISBN Numarası Güncelleme Fonksiyonumuz
    print("Update Book Name:", end=" ")
    print(getBooksFromBookID(id))#Belirtilen ID'ye göre işlem yapılacak veriyi getirdik.
    isbn = int(input("Update Book ISBN:"))
    cur.execute("Update Books set ISBN={} where BookID = {}".format(isbn, id))#Güncelleme işlemi yapıldı
    db.commit()
    print("Book Updated")

def checkBookStatusFromID(id):#Kitap Statusu Kontrol Fonksiyonumuz
    cur.execute("Select Status from Books where BookID = ?  ", (id,))#Belirtilen parametreye göre arama yaptık.
    data = cur.fetchone()
    print(data)
    if(data[0] == "Free"):#Eğer Status uygunsa True,değilse False gönderdik.
        return True
    else:
        return False
