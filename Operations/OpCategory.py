from Database import Database

database = Database()

class Category:
    def addCategory(self):
        name = input("Category Name:")
        database.cur.execute("Insert into Categories(Name) values(?)",[name])
        database.db.commit()
        print("Category Added..")

    def getCategoriesAll(self):
        database.cur.execute("Select * from Categories")
        datas = database.cur.fetchall()
        return datas

    def getCategoriesFromName(self,text):
        database.cur.execute("Select * from Categories where Name Like '%{}%' ".format(text))
        datas = database.cur.fetchall()
        return datas

    def getCategoriesFromID(self,id):
        database.database.cur.execute("Select * from Categories where CategoryID = ?  ",(id,))
        data = database.cur.fetchone()
        return data

    def deleteCategoryFromID(self,id):
        print("Category to be deleted:",end=" ")
        print(self.getCategoriesFromID(id))
        database.cur.execute("Delete from Categories where CategoryID = ?",(id,))
        database.db.commit()
        print("DEleted")

    def updateCategoryFromID(self,id):
        print("Category to be updated:", end=" ")
        print(self.getCategoriesFromID(id))
        name = input("Update Category Name:")
        database.cur.execute("Update Categories set Name='{}' where CategoryID = {}".format(name, id))
        database.db.commit()
        print("Updated")
