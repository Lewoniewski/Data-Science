utas_szam = int(input("Kérjük, adja meg az utasok számát: "))

if utas_szam <= 35:
    print("Válassza a Buszt az utazáshoz.")
elif utas_szam <= 120:
    print("Válassza a Vonatot az utazáshoz.")
else:
    print("Válassza a Repülőgépet az utazáshoz.")
