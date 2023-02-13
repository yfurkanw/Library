from Operations.OpMember import  *
from Operations.OpCategory import *
from Operations.OpBooks import *
from Operations.OpTookBooks import *
from Operations.OpReceivedBooks import *
from Operations.OpReturnedbooks import *

BookOperations = Book()
CategoryOperations = Category()
Member = MemberClass()
def librarianMain():
    print("Welcome to Librarian Screen\n")
    while(True):
        print("1-Member Process\n2-Category Process\n3-Book Category\n4-Take,Reserve,Go Back\n5-Exit")
        selection = int(input("Enter Your Selection:"))
        if(selection == 1):
            print("\n1-Add Member(Librarian)\n2-Add Member(User)\n3-All Member List\n4-Member Search(ID)\n5-Member Search(Last Name)")
            member_selection = int(input("Enter Your Selection:"))
            if(member_selection == 1):
                Member.MemberSignUp()
            elif(member_selection == 2):
                Member.MemberSignUpLibrarian()
            elif(member_selection == 3):
                Member.getMemberAll()
            elif(member_selection == 4):
                id = int(input("Enter Member ID"))
                print(Member.getMemberfromID(id))
            elif(member_selection == 5):
                text = input("Enter Member Last Name:")
                print(Member.getMemberFromLastName(text))
            else:
                print("Wrong Entry")
        elif(selection == 2):
            print("\n1-Add Category\n2-All Category List\n3-Category Search(ID)\n4-Category Search(Name)")
            category_selection = int(input("Enter Your Selection:"))
            if(category_selection == 1):
                CategoryOperations.addCategory()
            elif(category_selection == 2):
                print(CategoryOperations.getCategoriesAll())
            elif(category_selection == 3):
                id = int(input("Kategori  ID'si giriniz:"))
                print(CategoryOperations.getCategoriesFromID(id))
            elif(category_selection == 4):
                text = input("Kategori Adını Giriniz:")
                print(Member.getMemberFromLastName(text))

        elif(selection == 3):
            print("\n1-Add Book\n2-Get All Book List\n3-Search Book(ID)"
                  "\n4-Search Book(Name)\n5-Search Book(Author)\n6-Search Book(Category ID)"
                  "\n7-Update Book Name(ID)\n8-Update Book Author(ID)\n9-Delete Book(ID)")

            book_selection = int(input("Enter Your Selection:"))
            if(book_selection == 1):
                BookOperations.addBook()
            elif(book_selection == 2):
                print(BookOperations.getBooksAll())
            elif(book_selection == 3):
                id = int(input("Enter Book ID:"))
                print(BookOperations.getBooksFromBookID(id))
            elif(book_selection == 4):
                name = input("Enter Book Name:")
                print(BookOperations.getBooksFromName(name))
            elif(book_selection == 5):
                name = input("Enter Book Author:")
                print(BookOperations.getBooksFromAuthor(name))
            elif(book_selection == 6):
                id = int(input("Enter Book Category ID:"))
                print(BookOperations.getBooksFromCategoryID(id))
            elif(book_selection == 7):
                id = int(input("Enter Book ID"))
                BookOperations.updateBookNameFromID(id)
            elif(book_selection == 8):
                id = int(input("Enter Book ID:"))
                BookOperations.updateBookAuthorFromID(id)
            elif(book_selection == 9):
                id = int(input("Enter Book ID:"))
                BookOperations.deleteBookFromID(id)
            else:
                print("Wrong Process")
        elif(selection == 4):
            print("\n1-Take Book\n2-Reserve Book\n3-Book Take Again:")
            book_process=int(input("Enter Your Selection:"))
            if(book_process == 1):
                TookBook.addTook()
            elif(book_process == 2):
                TookBook.addReceived()
            elif(book_process == 3):
                TookBook.addReturned()

        elif(selection == 5):
            break


