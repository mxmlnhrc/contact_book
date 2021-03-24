from Database import AddPerson, CreateDatabase
import phonenumbers

while True:
    firstname = str(input("Firstname:\n"))
    lastname = str(input("Lastname:\n"))
    while True:
        phone_number = str(input("Phone number:\n"))
        try:
            phone_number = phonenumbers.parse(phone_number, None)
            if phonenumbers.is_possible_number(phone_number):
                if phonenumbers.is_valid_number(phone_number):
                    phone = phone_number
                    break
                else:
                    print("This number is not valid.\nPlease try again.")
            else:
                print("This number is to short/long.\nPlease try again.")
        except phonenumbers.phonenumberutil.NumberParseException as e:
            print(e)

    print("Data that is submitted:")
    print(f"Firstname: {firstname} | Lastname: {lastname} | Phonenumber: ")