# main User program
import shelve       # for filing

from PhoneBook import PhoneBook, InvalidPhoneException
from User import User
from Address import InvalidCountryNameException, InvalidCityNameException, InvalidZipException
from Person import InvalidGenderException


if __name__ == '__main__':

    # load registered users file
    users = shelve.open("Users")
    while True:     # Program don't continue(means will keep looping) until user don't LOGIN
        print('''
        1 - Login
        2 - Sign Up
        3 - Exit
        ''')
        choice = input("Enter Choice")

        if choice == '1':
            username = input("Username")
            password = input("Password")
            if len(users) == 0:
                print("No Users Registerd Currently")
                continue
            try:
                if users[username]:
                    user = users[username]
                    if user.validate(username, password):
                        print("********LOGGED IN ********")
                        break
                    else:
                        print("Incorrect Password")
            except KeyError:
                print("User not exist")
        elif choice == '2':
            print("******** SIGN UP ********")
            first_name = input("First Name\t: ")
            last_name = input("Last Name\t: ")
            gender = input("M / F\t: ")
            username = input("Username")
            password = input("Password")
            try:
                user = User(first_name, last_name, gender, username, password)
                users[username] = user
            except:
                print("Invalid User Data")
        elif choice == '3':
            exit(0)
        else:
            print("Invalid Choice")

    """
    PHONE BOOK IS NOW AVAILABLE TO USER
    MENU WILL BE SHOWN TO USER, IF USER HAS SUCCESSFULLY SIGNED IN ABOVE
    """

    # load users phone book
    contacts = shelve.open(username+"PhoneBook", writeback=True)

    while True:

        print("""
        1 - Create New Contact
        2 - Search For Contact
        3 - Update Contact
        4 - Delete Contact
        5 - List All Contacts
        6 - Logout
        """)
        choice = (input("\nEnter Choice >> "))

        if choice == '1':  # CREATE NEW CONTACT

            first_name = input("First Name\t: ")
            last_name = input("Last Name\t: ")
            gender = input("M / F\t: ")
            phone = input("Phone(03xx-xxxxxxx)\t: ")
            city = input("City\t: ")
            country = input("Country\t: ")
            zip_code = input("Zip Code\t: ")
            print("--------------")
            try:  # try to create new object
                contact = PhoneBook(first_name, last_name, gender, phone, city, country, zip_code)
            except InvalidPhoneException as e:
                print(e)
                continue
            except InvalidGenderException as e:
                print(e)
                continue
            except InvalidZipException as e:
                print(e)
                continue
            except InvalidCityNameException as e:
                print(e)
                continue
            except InvalidCountryNameException as e:
                print(e)
                continue    # go back and show the menu again

            # reached here meaning no exception occurred above

            if len(contacts) == 0 or not contacts[contact.phone]:  # if book empty or same contact number not already
                contacts[contact.phone] = contact
                print("CONTACT SUCCUSSFULLY ADDED TO YOUR PHONE BOOK")
            else:
                print("Phone Number already in contacts")

        elif choice == '2':  # SEARCH CONTACT

            first_name = input("First Name\t: ")
            last_name = input("Last Name\t: ")

            if len(contacts) > 0:   # if book is not empty
                for contact in contacts:    # go through every contact
                    #  if contact found, print it
                    if contacts[contact].person.first_name == first_name.title() \
                            and contacts[contact].person.last_name == last_name.title():
                        print(contacts[contact])
                else:
                    print("Contact Not Found")
            else:
                print("Phone Book Empty")

        elif choice == '3':  # UPDATE CONTACT

            first_name = input("First Name\t: ")
            last_name = input("Last Name\t: ")
            if len(contacts) > 0:   # if book is not empty
                for contact in contacts:    # go through every contact
                    # if contact matches user input, then try to update it
                    if contacts[contact].person.first_name == first_name.title() \
                            and contacts[contact].person.last_name == last_name.title():
                        print("--Enter details to update. Leave empty to not Change--")

                        phone = input("Phone(03xx-xxxxxxx)\t: ")
                        city = input("City\t: ")
                        country = input("Country\t: ")
                        zip_code = input("Zip Code\t: ")

                        if bool(phone):
                            print("inside phone ifs")
                            try:
                                contacts[contact].phone = phone
                            except InvalidPhoneException as e:
                                print(e)
                        if bool(city):
                            try:
                                contacts[contact].address.city = city
                            except InvalidCityNameException as e:
                                print(e)
                        if bool(country):
                            try:
                                contacts[contact].address.country = country
                            except InvalidCountryNameException as e:
                                print(e)
                        if bool(zip_code):
                            try:
                                contacts[contact].address.zip = zip_code
                            except InvalidZipException as e:
                                print(e)
                        contacts.sync()     # save shelve
                        break  # go to menu again
                else:
                    print("Contact Not Found")
            else:
                print("Phone Book Empty")

        elif choice == '4':  # DELETE CONTACT

            first_name = input("First Name\t: ")
            last_name = input("Last Name\t: ")
            if len(contacts) > 0:   # if book is not empty
                for contact in contacts:    # go through every contact
                    # if contact matches user input then delete it
                    if contacts[contact].person.first_name == first_name.title() \
                            and contacts[contact].person.last_name == last_name.title():
                        del contacts[contact]
                        print("Contact Deleted Successfully")
                        break  # go to menu again
                else:
                    print('Contact Not Found')
            else:
                print("Phone Book Empty")

        elif choice == '5':  # SHOW ALL CONTACTS\

            print("Showing all contacts\n")
            for contact in contacts:
                print(contacts[contact])

        elif choice == '6':  # EXIT

            print("Exiting")
            exit(0)
        else:

            print("Invalid Choice")