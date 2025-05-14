broj_putnika = int(input("Unesite broj putnika: "))

if broj_putnika <= 35:
    print("Odaberite Autobus za putovanje.")
elif broj_putnika <= 120:
    print("Odaberite Vlak za putovanje.")
else:
    print("Odaberite Zrakoplov za putovanje.")