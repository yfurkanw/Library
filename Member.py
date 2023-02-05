from Operations.OpMember import  *
from Operations.OpCategory import *
from Operations.OpBooks import *
from Operations.OpTookBooks import *
from Operations.OpReceivedBooks import *
from Operations.OpReturnedbooks import *

def memberMain():
    print("Welcome to Member Screen\n")
    while(True):
        print("\n1-Category Process\n2-Book Process\n3-Take,Reserve,Go Back\n4-Çıkış")
        selection = int(input("Enter Your Selection:"))

        if(selection == 1):
            print("\n1-All Category List\n2-Category Search(ID)\n3-Category Search(Name)")
            category_selection = int(input("Enter Your Selection:"))
            if(category_selection == 1):
                print(getCategoriesAll())
            elif(category_selection == 2):
                id = int(input("Enter ID of Category you want to search"))
                print(getCategoriesFromID(id))
            elif(category_selection == 3):
                text = input("Enter Name of CAtegory you want to search")
                print(getMemberFromLastName(text))

        elif(selection == 2):
            print("\n1-Get All Book List\n2-Search Book(ID)"
                  "\n3-Search Book(Name)\n4-Search Book(Author)\n5-Search Book(Category ID)")

            book_selection = int(input("Enter Your Selection:"))
            if(book_selection == 1):
                print(getBooksAll())
            elif(book_selection == 2):
                id = int(input("Enter the ID of the book you want to search"))
                print(getBooksFromBookID(id))
            elif(book_selection == 3):
                name = input("Enter the name of the book you want to search:")
                print(getBooksFromName(name))
            elif(book_selection == 4):
                name = input("Enter the author of the book you want to search:")
                print(getBooksFromAuthor(name))
            elif(book_selection == 5):
                id = int(input("Enter the ID of the category of the book you want to search:"))
                print(getBooksFromCategoryID(id))
            else:
                print("Wrong Process")
        elif(selection == 3):
            print("\n1-Reserve the Book.")
            bookprocess=int(input("Enter Your Selection:"))
            if(bookprocess == 1):
                print(addReceived())
        elif(selection == 4):
            break
