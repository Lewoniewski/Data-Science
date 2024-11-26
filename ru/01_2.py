passazhiry = int(input("Введите количество пассажиров: "))

if passazhiry <= 35:
    print("Выберите Автобус для поездки.")
elif passazhiry <= 120:
    print("Выберите Поезд для поездки.")
else:
    print("Выберите Самолёт для поездки.")