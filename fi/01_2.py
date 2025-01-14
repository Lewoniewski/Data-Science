matkustajia = int(input("Syötä matkustajien lukumäärä: "))

if matkustajia <= 35:
    print("Valitse Linja-auto matkalle.")
elif matkustajia <= 120:
    print("Valitse Juna matkalle.")
else:
    print("Valitse Lentokone matkalle.")
