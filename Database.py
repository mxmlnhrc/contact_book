import os
import sys
import sqlite3


class Database:
    def CreateDatabase(name):
        # Check if database exists
        if os.path.exists(name + ".db"):
            print("Database already exists.")
            sys.exit(0)

        connection = sqlite3.connect(name + ".db")

        cursor = connection.cursor()

        sql = (
            "CREATE TABLE personen(" "surname TEXT," "firstname TEXT," "phone INTERGER)"
        )

        cursor.execute(sql)
        connection.commit()

        print("Sucessfully created a database")

    # def AddPerson(firstname, surname, phone):
