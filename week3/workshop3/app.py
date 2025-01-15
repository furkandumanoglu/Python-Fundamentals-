from donations_pkg.homepage import show_homepage, show_donations
from donations_pkg.user import login, register

database = {"admin": "password123"}
donations = []
authorized_user = ""

while True:
    show_homepage()
    option = input("Choose an option: ")
    if option == "1":
        username = input("Enter username: ")
        password = input("Enter password: ")
        authorized_user = login(database, username, password)
    elif option == "2":
        username = input("Choose a username: ")
        password = input("Choose a password: ")
        result = register(database, username)
        if result:
            database[username] = password
            authorized_user = result
            print(f"{username} has been registered successfully.")
    elif option == "3":
        if authorized_user == "":
            print("You must be logged in to donate.")
        else:
            donation_amt = float(input("Enter amount to donate: "))
            donations.append(f"{authorized_user} donated ${donation_amt:.2f}")
            print("Thank you for your donation!")
    elif option == "4":
        show_donations(donations)
    elif option == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid option, please try again.")