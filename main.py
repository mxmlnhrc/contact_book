import os, sys
from Database import AddPerson, GetAllItems, GetItem
from security import check_name
import phonenumbers
import time

database = "contact_book"


# add a person, with verfication
def add_peron():
    while True:
        firstname = str(input("Firstname:\n"))
        if check_name(firstname) == True:
            break
        print("The Name submitted was not valid!\nPlease try again:")
    while True:
        lastname = str(input("Lastname:\n"))
        if check_name(lastname) == True:
            break
        print("The Name submitted was not valid!\nPlease try again:")
    while True:
        phone_number = str(input("Phone number:\n"))
        phone = phone_number
        try:
            phone_number = phonenumbers.parse(phone_number, None)
            if phonenumbers.is_possible_number(phone_number):
                if phonenumbers.is_valid_number(phone_number):
                    phone = phone
                    break
                else:
                    print("This number is not valid.\nPlease try again.")
            else:
                print("This number is to short/long.\nPlease try again.")
        except phonenumbers.phonenumberutil.NumberParseException as e:
            print(e)

    print("")
    print("Data that is submitted:")
    print(
        f"Firstname: {firstname} | Lastname: {lastname} | Phonenumber: {phone}"
    )
    print("")
    print("yes or no")

    while True:
        check_for_submission = input(
            "Do you want to submit this contact?\nAnswer with yes or no:\n"
        ).lower()
        if check_for_submission == "yes" or check_for_submission == "no":
            if check_for_submission == "yes":
                AddPerson(firstname=firstname, lastname=lastname, phone=phone)
                break
            else:
                print("Okay, we will send you back to the beginning")
                add_peron()


def get_all():
    GetAllItems()
    user_in = input("Type any key to continue")
    os.system("cls")


def get_item():
    user_in = input(
        "what do you want to look after?\nFirstname, Lastname or Phonenumber\n"
    )
    if user_in.lower() == "firstname":
        while True:
            firstname = input("What is the firstname?\n")
            if check_name(firstname) == True:
                os.system("cls")
                GetItem(db=database, firstname=firstname)
                user_in = input("Press any key to continue\n")
                break
    elif user_in.lower() == "lastname":
        while True:
            lastname = input("What is the lastname?\n")
            if check_name(lastname) == True:
                os.system("cls")
                GetItem(db=database, lastname=lastname)
                user_in = input("Press any key to continue\n")
                break


while True:
    user_in = input(
        "What do you want to do?\n 1: Add a contact\n 2: Get all contacts\n 3: Get a contacts based on your input\n"
    )

    if user_in == '1':
        os.system("cls")
        add_peron()
    elif user_in == '2':
        os.system("cls")
        get_all()
    elif user_in == '3':
        os.system("cls")
        get_item()

    elif user_in.lower() == 'exit':
        print("Okay, Good Bye and see you soon!")
        sys.exit(1)
    else:
        os.system("cls")
        print("Please select a valid code.")
        time.sleep(1)
        os.system("cls")

    os.system("cls")