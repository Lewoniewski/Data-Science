passengers = int(input("أدخل عدد الركاب: "))

if passengers <= 35:
    print("اختر الحافلة للسفر.")
elif passengers <= 120:
    print("اختر القطار للسفر.")
else:
    print("اختر الطائرة للسفر.")
