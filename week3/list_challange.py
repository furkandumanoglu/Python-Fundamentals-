import random

diamonds = ["AD", "2D", "3D", "4D", "5D", "6D", "7D", "8D", "9D", "10D", "JD", "QD", "KD"]
hand = []

while diamonds:
    user_input = input("Press Enter to pick card, or type 'Q' to quit: ")
    
    if user_input.upper() == "Q":
        print("You chose to quit.")
        break
    else:
        card = random.choice(diamonds) 
        diamonds.remove(card)           
        hand.append(card)               
        print(f"Card picked: {card}")
        print(f"Remaining diamonds: {diamonds}")
        print(f"Cards in hand: {hand}")

if not diamonds:
    print("There are no more cards to pick.")