import sqlite3 as sql
db = sql.connect("libraryDb.sqlite")
cur = db.cursor()

def addCategory():
    name = input("Category Name:")
    cur.execute("Insert into Categories(Name) values(?)",[name])
    db.commit()
    print("Category Added..")

def getCategoriesAll():
    cur.execute("Select * from Categories")
    datas = cur.fetchall()
    return datas

def getCategoriesFromName(text):
    cur.execute("Select * from Categories where Name Like '%{}%' ".format(text))
    datas = cur.fetchall()
    return datas

def getCategoriesFromID(id):
    cur.execute("Select * from Categories where CategoryID = ?  ",(id,))
    data = cur.fetchone()
    return data

def deleteCategoryFromID(id):
    print("Category to be deleted:",end=" ")
    print(getCategoriesFromID(id))
    cur.execute("Delete from Categories where CategoryID = ?",(id,))
    db.commit()
    print("DEleted")

def updateCategoryFromID(id):
    print("Category to be updated:", end=" ")
    print(getCategoriesFromID(id))
    name = input("Update Category Name:")
    cur.execute("Update Categories set Name='{}' where CategoryID = {}".format(name, id))
    db.commit()
    print("Updated")
