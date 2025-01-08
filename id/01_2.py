jumlah_penumpang = int(input("Masukkan jumlah penumpang: "))

if jumlah_penumpang <= 35:
    print("Pilih Bus untuk perjalanan.")
elif jumlah_penumpang <= 120:
    print("Pilih Kereta untuk perjalanan.")
else:
    print("Pilih Pesawat untuk perjalanan.")
