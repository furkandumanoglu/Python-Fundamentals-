import random

high_score = 0


def dicegame():
    global high_score

    while True:
        print("1) Roll Dice")
        print("2) Leave Game")
        choice = input("Enter your choice:")

        if choice == "1":
            roll1 = random.randint(1, 6)
            roll2 = random.randint(1, 6)
            total = roll1 + roll2

            print(f"\n You rolled a {roll1} and a {roll2} \nTotal: {total}")

            if total > high_score:
                high_score = total
                print("New High Score!!!!")

            else:
                print("Try again to beat high score!!")
        elif choice == "2" :
            print("Thanks for playing!!!")
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")
dicegame()