passagers = int(input("Entrez le nombre de passagers : "))

if passagers <= 35:
    print("Choisissez le Bus pour votre voyage.")
elif passagers <= 120:
    print("Choisissez le Train pour votre voyage.")
else:
    print("Choisissez l'Avion pour votre voyage.")
