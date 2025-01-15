def show_homepage():
    print("=== DonateMe Homepage ===")
    print("1. Login || 2. Register")
    print("3. Donate|| 4. Show Donations")
    print("5. Exit")

def show_donations(donations):
    if not donations:
        print("Currently, there are no donations.")
    else:
        print("\n--- All Donations ---")
        for donation in donations:
            print(donation)