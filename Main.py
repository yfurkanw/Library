from Initialize import initialize
from Operations.OpMember import *
import Librarian
import Member

initialize()#Initialize.py dosyasındaki initiliaze fonksiyonunu çağırdık. Sql komutlarımız çalıştı.

MemberOperations = MemberClass()


if(__name__ == '__main__'):
    print("Welcome to Library Management System")
    print("1-Sign In\n2-Sign Up")
    secim = int(input("Insert your Choice"))
    if(secim == 1):
        Mail = input("Insert Your Mail:")
        Password = input("Insert your Password:")
        sonuc = MemberOperations.MemberLogin(Mail,Password) #MemberLogin fonksiyonunun geri döndürdüğü iki değeri(True/False,Information) aldık.
        if(sonuc == True): #Giriş başarılı ise
            print("Login Succesesful")
            if(MemberOperations.Type == "Librarian"): #Kullanıcı eğer Librarian ise
                Librarian.librarianMain() # Librarian UI yı çağırdık.
            elif(MemberOperations.Type == "User"): #Kullanıcı eğer User ise
                Member.memberMain() #Member UI yı çağırdık.
        else:
            print("Wrong User Mail or Password ")
    elif(secim == 2):
        MemberOperations.MemberSignUp() #User Kullanıcısını kaydetmeme fonksiyonu.1


