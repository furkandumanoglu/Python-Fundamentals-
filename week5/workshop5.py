import random

def guess_random_number(tries, start, stop):
    target = random.randint(start, stop)
    while tries != 0:
        print(f"There are {tries} tries remaining")
        guess = int(input(f"Guess a number between {start} and {stop}: "))
        if guess == target:
            print("You guessed the number!!")
            return
        elif guess < target:
            print("Guess higher than that!")
        else:
            print("Guess lower than that!")
        tries -= 1

    print(f"You ran out of tries, the number was {target}")


def guess_random_num_linear(tries, start, stop):
    target = random.randint(start, stop)
    for guess in range(start, stop + 1):
        print(f"Tries: {tries}")
        print(f"Guess: {guess}")
        if guess == target:
            print("Congratulations!")
            return
        tries -= 1
        if tries == 0:
            break

    print(f"You ran out of tries, the number was {target}")


guess_random_number(520, 0, 100)