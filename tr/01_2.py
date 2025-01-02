yolcu_sayisi = int(input("Lütfen yolcu sayısını giriniz: "))

if yolcu_sayisi <= 35:
    print("Seyahat için Otobüs'ü seçin.")
elif yolcu_sayisi <= 120:
    print("Seyahat için Tren'i seçin.")
else:
    print("Seyahat için Uçak'ı seçin.")
