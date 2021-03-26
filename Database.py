import os
from sqlite3.dbapi2 import Cursor
import sys
import sqlite3
from tabulate import tabulate


def create_table(cursor, cats):
    table = []

    for dsatz in cursor:
        table.append([dsatz[0], dsatz[1], dsatz[2]])

    print(tabulate(table, headers=cats, tablefmt="pretty"))


def CreateDatabase(db="contact_book"):
    # Check if database exists
    if os.path.exists(db + ".db"):
        print("Database already exists.")
        sys.exit(0)

    connection = sqlite3.connect(db + ".db")
    cursor = connection.cursor()

    sql = "CREATE TABLE contacts(" "lastname TEXT," "firstname TEXT," "phone INTEGER)"

    cursor.execute(sql)
    connection.commit()

    print(f"Sucessfully created a database {db}.db")


def AddPerson(firstname, lastname, phone, db="contact_book"):
    categories = ["Lastname", "Firstname", "Phonenumber"]
    if not os.path.exists(db + ".db"):
        CreateDatabase(db)

    phone = int(phone)
    connection = sqlite3.connect(db + ".db")
    cursor = connection.cursor()

    sql = f"INSERT INTO contacts VALUES('{lastname}', '{firstname}', '{phone}')"

    cursor.execute(sql)
    connection.commit()

    print(f"{firstname} was sucessfully added to your conatct book.")


def GetAllItems(db="contact_book"):
    connection = sqlite3.connect(db + ".db")
    cursor = connection.cursor()

    # SQL-Request
    sql = "SELECT * FROM contacts"

    # Send of an SQL request
    # getting the Data
    cursor.execute(sql)

    # return the results
    categories = ["Lastname", "Firstname", "Phonenumber"]
    create_table(cursor=cursor, cats=categories)

    # close the connection
    connection.close()


def GetItem(db="contact_book", firstname="*", lastname="", phone=""):
    db = db + ".db"
    connection = sqlite3.connect(db)
    cursor = connection.cursor()

    # sql = f"SELECT * FROM {db} WHERE firstname = {firstname} AND lastname = {lastname} AND phone = {phone};"
    sql = f"SELECT * FROM contacts WHERE lastname=? OR firstname=? OR phone=?"

    cursor.execute(sql, (
        lastname,
        firstname,
        phone,
    ))

    categories = ["Lastname", "Firstname", "Phonenumber"]
    create_table(cursor=cursor, cats=categories)
