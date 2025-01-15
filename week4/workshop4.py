class User:
    def __init__(self, name, pin, password):
        self.name = name
        self.pin = pin
        self.password = password

    def change_name(self, new_name):
        self.name = new_name

    def change_pin(self, new_pin):
        self.pin = new_pin

    def change_password(self, new_password):
        self.password = new_password

""" Driver Code for Task 1 """
 
#user1 = User("Bob", 1234, "password")
#print(user1.name, user1.pin, user1.password)

""" Driver Code for Task 2 """

#user1 = User("Bob", 1234, "password")
#print(user1.name, user1.pin, user1.password)
#user1.change_name("Alice")
#user1.change_pin(4321)
#user1.change_password("newpassword")
#print(user1.name, user1.pin, user1.password)


class BankUser(User):
    def __init__(self, name, pin, password):
        super().__init__(name, pin, password)
        self.balance = 0

    def show_balance(self):
        print(f"{self.name}'s balance: ${self.balance}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{self.name} deposited ${amount}.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"{self.name} withdrew ${amount}.")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    def transfer_money(self, other_user, amount):
        pin = int(input(f"Enter PIN for {self.name}: "))
        if pin == self.pin and amount <= self.balance:
            self.balance -= amount
            other_user.balance += amount
            print(f"{self.name} transferred ${amount} to {other_user.name}.")
            return True
        else:
            print("Transfer failed. Incorrect PIN try againn .")
            return False

    def request_money(self, other_user, amount):
        pin = int(input(f"Enter PIN for {other_user.name} to approve request: "))
        if pin == other_user.pin:
            password = input(f"Enter password for {self.name} to confirm request: ")
            if password == self.password and amount <= other_user.balance:
                other_user.balance -= amount
                self.balance += amount
                print(f"{self.name} requested ${amount} from {other_user.name}.")
                return True
            else:
                print("Request failed. Incorrect password")
                return False
        else:
            print("Request failed. Incorrect PIN.")
            return False

""" Driver Code for Task 3 """

#bank_user = BankUser("Bob", 1234, "password")
#print(bank_user.name, bank_user.pin, bank_user.password, bank_user.balance)

""" Driver Code for Task 4 """

#bank_user = BankUser("Bob", 1234, "password")
#bank_user.show_balance()
#bank_user.deposit(100)
#bank_user.show_balance()
#bank_user.withdraw(50)
#bank_user.show_balance()


""" Driver Code for Task 5 """

user1 = BankUser("Alice", 1111, "alicepass")
user2 = BankUser("Bob", 2222, "bobpass")
user2.deposit(5000)
user2.show_balance()
user1.show_balance()
if user2.transfer_money(user1, 500):
    user1.show_balance()
    user2.show_balance()
if user2.request_money(user1, 200):
   user1.show_balance()
   user2.show_balance()