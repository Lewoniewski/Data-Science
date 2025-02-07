passagiers = int(input("Voer het aantal passagiers in: "))

if passagiers <= 35:
    print("Kies de Bus voor de reis.")
elif passagiers <= 120:
    print("Kies de Trein voor de reis.")
else:
    print("Kies het Vliegtuig voor de reis.")
