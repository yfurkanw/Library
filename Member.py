from Operations.OpCategory import *
from Operations.OpReceivedBooks import *
from Operations.OpReturnedbooks import *

BookOperations = Book()
CategoryOperations = Category()
Member = MemberClass()
ReceivedOp = Received()
def memberMain():
    print("Welcome to Member Screen\n")
    while(True):
        print("\n1-Category Process\n2-Book Process\n3-Take,Reserve,Go Back\n4-Çıkış")
        selection = int(input("Enter Your Selection:"))

        if(selection == 1):
            print("\n1-All Category List\n2-Category Search(ID)\n3-Category Search(Name)")
            category_selection = int(input("Enter Your Selection:"))
            if(category_selection == 1):
                print(CategoryOperations.getCategoriesAll())
            elif(category_selection == 2):
                id = int(input("Enter ID of Category you want to search"))
                print(CategoryOperations.getCategoriesFromID(id))
            elif(category_selection == 3):
                text = input("Enter Name of CAtegory you want to search")
                print(CategoryOperations.getCategoriesFromName(text))

        elif(selection == 2):
            print("\n1-Get All Book List\n2-Search Book(ID)"
                  "\n3-Search Book(Name)\n4-Search Book(Author)\n5-Search Book(Category ID)")

            book_selection = int(input("Enter Your Selection:"))
            if(book_selection == 1):
                print(BookOperations.getBooksAll())
            elif(book_selection == 2):
                id = int(input("Enter the ID of the book you want to search"))
                print(BookOperations.getBooksFromBookID(id))
            elif(book_selection == 3):
                name = input("Enter the name of the book you want to search:")
                print(BookOperations.getBooksFromName(name))
            elif(book_selection == 4):
                name = input("Enter the author of the book you want to search:")
                print(BookOperations.getBooksFromAuthor(name))
            elif(book_selection == 5):
                id = int(input("Enter the ID of the category of the book you want to search:"))
                print(BookOperations.getBooksFromCategoryID(id))
            else:
                print("Wrong Process")
        elif(selection == 3):
            print("\n1-Reserve the Book.")
            bookprocess=int(input("Enter Your Selection:"))
            if(bookprocess == 1):
                print(ReceivedOp.addReceived())
        elif(selection == 4):
            break

