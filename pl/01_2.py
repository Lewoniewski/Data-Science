pasazerowie = int(input("Wprowadź liczbę pasażerów: "))

if pasazerowie <= 35:
    print("Wybierz Autobus jako środek transportu.")
elif pasazerowie <= 120:
    print("Wybierz Pociąg jako środek transportu.")
else:
    print("Wybierz Samolot jako środek transportu.")