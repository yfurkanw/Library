from Operations.OpMember import  *
from Operations.OpCategory import *
from Operations.OpBooks import *
from Operations.OpTookBooks import *
from Operations.OpReceivedBooks import *
from Operations.OpReturnedbooks import *
def librarianMain():
    print("Welcome to Librarian Screen\n")
    while(True):
        print("1-Member Process\n2-Category Process\n3-Book Category\n4-Take,Reserve,Go Back\n5-Exit")
        secim = int(input("Enter Your Selection:"))
        if(secim == 1):
            print("\n1-Add Member(Librarian)\n2-Add Member(User)\n3-All Member List\n4-Member Search(ID)\n5-Member Search(Last Name)")
            member_selection = int(input("Enter Your Selection:"))
            if(member_selection == 1):
                MemberSignUp()
            elif(member_selection == 2):
                MemberSignUpLibrarian()
            elif(member_selection == 3):
                getMemberAll()
            elif(member_selection == 4):
                id = int(input("Enter Member ID"))
                print(getMemberfromID(id))
            elif(member_selection == 5):
                text = input("Enter Member Last Name:")
                print(getMemberFromLastName(text))
            else:
                print("Wrong Entry")
        elif(secim == 2):
            print("\n1-Add Category\n2-All Category List\n3-Category Search(ID)\n4-Category Search(Name)")
            category_selection = int(input("Enter Your Selection:"))
            if(category_selection == 1):
                addCategory()
            elif(category_selection == 2):
                getCategoriesAll()
            elif(category_selection == 3):
                id = int(input("Kategori  ID'si giriniz:"))
                print(getCategoriesFromID(id))
            elif(category_selection == 4):
                text = input("Kategori Adını Giriniz:")
                print(getMemberFromLastName(text))

        elif(secim == 3):
            print("\n1-Add Book\n2-Get All Book List\n3-Search Book(ID)"
                  "\n4-Search Book(Name)\n5-Search Book(Author)\n6-Search Book(Category ID)"
                  "\n7-Update Book Name(ID)\n8-Update Book Author(ID)\n9-Delete Book(ID)")

            kitap_secim = int(input("Enter Your Selection:"))
            if(kitap_secim == 1):
                addBook()
            elif(kitap_secim == 2):
                print(getBooksAll())
            elif(kitap_secim == 3):
                id = int(input("Kitap  ID'si giriniz:"))
                print(getBooksFromBookID(id))
            elif(kitap_secim == 4):
                name = input("Kitap  Adını giriniz:")
                print(getBooksFromName(name))
            elif(kitap_secim == 5):
                name = input("Kitap  Authhor giriniz:")
                print(getBooksFromAuthor(name))
            elif(kitap_secim == 6):
                id = int(input("Kitap  Category ID'si giriniz:"))
                print(getBooksFromCategoryID(id))
            elif(kitap_secim == 7):
                id = int(input("Kitap  ID'si giriniz:"))
                updateBookNameFromID(id)
            elif(kitap_secim == 8):
                id = int(input("Kitap  ID'si giriniz:"))
                updateBookAuthorFromID(id)
            elif(kitap_secim == 9):
                id = int(input("Kitap  ID'si giriniz:"))
                deleteBookFromID(id)
            else:
                print("Hatalı İşlem")
        elif(secim == 4):
            print("\n1-Kitap Kirala\n2-Kitap Rezerve Et\n3-Kitap Geri Al")
            kitap_islemler=int(input("Seçiminizi Giriniz:"))
            if(kitap_islemler == 1):
                addTook()
            elif(kitap_islemler == 2):
                addReceived()
            elif(kitap_islemler == 3):
                addReturned()

        elif(secim == 5):
            break


