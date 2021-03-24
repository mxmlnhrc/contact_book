import os
import sys
import sqlite3


class CreateDatabase:
    # Check if database exists
    if os.path.exists("contact_book.db"):
        print("Database already exists.")
        sys.exit(0)

    connection = sqlite3.connect("contact_book.db")

    cursor = connection.cursor()

    sql = "CREATE TABLE personen(" "surname TEXT," "firstname TEXT," "phone INTERGER)"

    cursor.execute(sql)
    connection.commit()

    print("Sucessfully imported a database")
