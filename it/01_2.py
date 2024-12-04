passeggeri = int(input("Inserisci il numero di passeggeri: "))

if passeggeri <= 35:
    print("Scegli l'Autobus per il viaggio.")
elif passeggeri <= 120:
    print("Scegli il Treno per il viaggio.")
else:
    print("Scegli l'Aereo per il viaggio.")