wizard = "Wizard"
elf = "Elf"
human = "Human"

wizard_hp = 70
wizard_damage = 150

elf_hp = 100
elf_damage = 100

human_damage = 20
human_hp = 150

dragon_hp = 300
dragon_damage = 50

while True:
    print("\nChoose your character:")
    print("1) Wizard")
    print("2) Elf")
    print("3) Human")

    choice = input("Enter 1, 2, 3: ")

    if choice == "1":
        character = wizard
        my_hp = wizard_hp
        my_damage = wizard_damage
        break
    elif choice == "2":
        character = elf
        my_hp = elf_hp
        my_damage = elf_damage
        break
    elif choice == "3":
        character = human
        my_hp = human_hp
        my_damage = human_damage
        break
    else:
        print("Unknown character. Try again.")

while True:
    dragon_hp -= my_damage
    print(f"The {character} damaged the Dragon!")
    print(f"Dragon's HP is now: {dragon_hp}")
    
    if dragon_hp <= 0:
        print("The Dragon has lost the battle!")
        break
    
    my_hp -= dragon_damage
    print(f"The Dragon attacks the {character}!")
    print(f"{character}'s HP is now: {my_hp}")
    
    if my_hp <= 0:
        print(f"The {character} has lost the battle!")
        break