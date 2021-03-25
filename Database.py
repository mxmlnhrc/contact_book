import os
from sqlite3.dbapi2 import Cursor
import sys
import sqlite3


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
    for dsatz in cursor:
        print(dsatz[0], dsatz[1], dsatz[2])

    # close the connection
    connection.close()