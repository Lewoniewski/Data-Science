numar_pasageri = int(input("Introduceți numărul de pasageri: "))

if numar_pasageri <= 35:
    print("Alegeți Autobuzul pentru călătorie.")
elif numar_pasageri <= 120:
    print("Alegeți Trenul pentru călătorie.")
else:
    print("Alegeți Avionul pentru călătorie.")