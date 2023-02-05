from Initialize import initialize
from Operations.OpMember import *
import Librarian
import Member

initialize()#Initialize.py dosyasındaki initiliaze fonksiyonunu çağırdık. Sql komutlarımız çalıştı.


userDict = {
    "ID":None,
    "FirstName":"",
    "LastName":"",
    "Type":"",
    "Mail":""
}#User işlemleri yapabilmek için bir sözlük oluşturduk.

if(__name__ == '__main__'):
    print("Welcome to Library Management System")
    print("1-Sign In\n2-Sign Up")
    secim = int(input("Insert your Choice"))
    if(secim == 1):
        Mail = input("Insert Your Mail:")
        Password = input("Insert your Password:")
        sonuc = MemberLogin(Mail,Password) #MemberLogin fonksiyonunun geri döndürdüğü iki değeri(True/False,Information) aldık.
        if(sonuc[0]== True): #Giriş başarılı ise
            print("Login Succesesful")
            userDict["ID"] = sonuc[1][0]
            userDict["FirstName"] = sonuc[1][1]
            userDict["LastName"] = sonuc[1][2]
            userDict["Type"] = sonuc[1][3]
            userDict["Mail"] = sonuc[1][4]
            if(userDict["Type"] == "Librarian"): #Kullanıcı eğer Librarian ise
                Librarian.librarianMain() # Librarian UI yı çağırdık.
            elif(userDict["Type"] == "User"): #Kullanıcı eğer User ise
                Member.memberMain() #Member UI yı çağırdık.
        else:
            print("Wrong User Mail or Password ")
    elif(secim == 2):
        MemberSignUp() #User Kullanıcısını kaydetmeme fonksiyonu.1


