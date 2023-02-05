import sqlite3 as sql
import hashlib
db = sql.connect("libraryDb.sqlite")
cur = db.cursor()

def MemberLogin(Mail,password):
    cur.execute(""" Select MemberID,FirstName,LastName,Type,Mail from Members where Mail = (?) and Password = (?) """
                ,(Mail,md5Hash(password)))
    memberData = cur.fetchone()
    if(memberData != None):
        return True,memberData
    else:
        return False,None

def MemberSignUp():
    firstNameTest = input("Input First Name:")
    LastNameTest = input("Input Last Name:")
    TypeTest = "User"
    MailTest = input("Input Mail:")
    Password = input("Input Password:")
    dataAddUserTest = [firstNameTest, LastNameTest, TypeTest, MailTest, md5Hash(Password),0]
    cur.execute(""" Insert into Members(FirstName,LastName,Type,Mail,Password,TookedBooks) values(?,?,?,?,?,?)""", dataAddUserTest)
    db.commit()
    print("Successfully saved...")

def MemberSignUpLibrarian():
    firstNameTest = input("Input First Name:")
    LastNameTest = input("Input Last Name:")
    TypeTest = "Librarian"
    MailTest = input("Input Mail:")
    Password = input("Input Password:")
    dataAddUserTest = [firstNameTest, LastNameTest, TypeTest, MailTest, md5Hash(Password),0]
    cur.execute(""" Insert into Members(FirstName,LastName,Type,Mail,Password,TookedBooks) values(?,?,?,?,?,?)""", dataAddUserTest)
    db.commit()
    print("Successfully saved...")

def getMemberAll():
    cur.execute("Select * from Members")
    userDatas = cur.fetchall()
    for i in userDatas:
        print(i)

def getMemberfromID(id):
    cur.execute("Select * from Members where MemberID = ?  ", (id,))
    data = cur.fetchone()
    return data

def getMemberFromLastName(text):
    cur.execute("Select * from Members where LastName Like '%{}%' ".format(text))
    datas = cur.fetchall()
    return datas

def checkcMemberTookingFromID(id):
    cur.execute("Select TookedBooks from Members where MemberID = ? ",(id,))
    data = cur.fetchone()
    if(data[0] <6):
        return True
    else:
        return False

def md5Hash(text):
    hasher = hashlib.md5()
    hasher.update(text.encode('utf-8'))
    hash = hasher.hexdigest()
    return hash
