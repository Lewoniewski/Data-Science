passengers = int(input("Enter the number of passengers: "))

if passengers <= 35:
    print("Choose Bus for travel.")
elif passengers <= 120:
    print("Choose Train for travel.")
else:
    print("Choose Plane for travel.")