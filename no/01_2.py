antall_passasjerer = int(input("Oppgi antall passasjerer: "))

if antall_passasjerer <= 35:
    print("Velg Buss for reisen.")
elif antall_passasjerer <= 120:
    print("Velg Tog for reisen.")
else:
    print("Velg Fly for reisen.")