import hashlib
from Database import Database
database = Database()

class MemberClass:

    def __init__(self):
        self.ID = None
        self.FirstName = ""
        self.LastName = ""
        self.Type = ""
        self.Mail = ""

    def MemberLogin(self,Mail,password):
        database.cur.execute(""" Select MemberID,FirstName,LastName,Type,Mail from Members where Mail = (?) and Password = (?) """
                    ,(Mail,self.md5Hash(password)))
        memberData = database.cur.fetchone()

        if(memberData != None):
            self.ID = memberData[0]
            self.FirstName = memberData[1]
            self.LastName = memberData[2]
            self.Type = memberData[3]
            self.Mail = memberData[4]
            return True
        else:
            return False

    def MemberSignUp(self):
        firstNameTest = input("Input First Name:")
        LastNameTest = input("Input Last Name:")
        TypeTest = "User"
        MailTest = input("Input Mail:")
        Password = input("Input Password:")
        dataAddUserTest = [firstNameTest, LastNameTest, TypeTest, MailTest, md5Hash(Password),0]
        database.cur.execute(""" Insert into Members(FirstName,LastName,Type,Mail,Password,TookedBooks) values(?,?,?,?,?,?)""", dataAddUserTest)
        database.db.commit()
        print("Successfully saved...")

    def MemberSignUpLibrarian(self):
        firstNameTest = input("Input First Name:")
        LastNameTest = input("Input Last Name:")
        TypeTest = "Librarian"
        MailTest = input("Input Mail:")
        Password = input("Input Password:")
        dataAddUserTest = [firstNameTest, LastNameTest, TypeTest, MailTest, md5Hash(Password),0]
        database.cur.execute(""" Insert into Members(FirstName,LastName,Type,Mail,Password,TookedBooks) values(?,?,?,?,?,?)""", dataAddUserTest)
        database.db.commit()
        print("Successfully saved...")

    def getMemberAll(self):
        database.cur.execute("Select * from Members")
        userDatas = database.cur.fetchall()
        for i in userDatas:
            print(i)

    def getMemberfromID(self,id):
        database.cur.execute("Select * from Members where MemberID = ?  ", (id,))
        data = database.cur.fetchone()
        return data

    def getMemberFromLastName(self,text):
        database.cur.execute("Select * from Members where LastName Like '%{}%' ".format(text))
        datas = database.cur.fetchall()
        return datas

    def checkcMemberTookingFromID(self,id):
        database.cur.execute("Select TookedBooks from Members where MemberID = ? ",(id,))
        data = database.cur.fetchone()
        if(data[0] <6):
            return True
        else:
            return False

    def md5Hash(self,text):
        hasher = hashlib.md5()
        hasher.update(text.encode('utf-8'))
        hash = hasher.hexdigest()
        return hash

