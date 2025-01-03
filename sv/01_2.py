passagerare = int(input("Ange antalet passagerare: "))

if passagerare <= 35:
    print("Välj Buss för resan.")
elif passagerare <= 120:
    print("Välj Tåg för resan.")
else:
    print("Välj Flyg för resan.")
