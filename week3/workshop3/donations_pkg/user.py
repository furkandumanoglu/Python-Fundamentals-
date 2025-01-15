def login(database, username, password):
    if username in database and database[username] == password:
        print(f"Welcome back, {username}!")
        return username
    elif username in database:
        print("Incorrect password. Please try again.")
        return 
    else:
        print("User not found. Please register.")
        return 

def register(database, username):
    if username in database:
        print("Username already registered.")
        return 
    else:
        return username