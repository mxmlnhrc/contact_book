import os
import sys
import sqlite3


def CreateDatabase(db="contact_book"):
    # Check if database exists
    if os.path.exists(db + ".db"):
        print("Database already exists.")
        sys.exit(0)

    connection = sqlite3.connect(db + ".db")

    cursor = connection.cursor()

    sql = "CREATE TABLE personen(" "lastname TEXT," "firstname TEXT," "phone INTERGER)"

    cursor.execute(sql)
    connection.commit()

    print("Sucessfully created a database")


def AddPerson(firstname, lastname, phone, db="contact_book"):
    if not os.path.exists(db + ".db"):
        CreateDatabase(db)
    else:
        print("Test")
