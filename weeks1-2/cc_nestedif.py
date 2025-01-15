priceIsRight = 15  

if priceIsRight < 5:
    print("Price is too low!")
elif priceIsRight >= 5 and priceIsRight <= 9:
    print("Price is almost right.")
elif priceIsRight == 10:
    print("Price is exactly right!")
else:
    print("Price is too high!")