x = 0

while x <= 10:
    x += 1
    if x < 5:
        print(x)
    elif x == 5 or (x >= 7 and x <= 8):
        print(f"x is bigger then or equal to 5, and less then or equal to 8, but not 6. It is: {x}")
    elif x == 6:
        print(x)
    elif x > 8:
        print(f"x is bigger than 8. It is: {x}")