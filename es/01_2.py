pasajeros = int(input("Ingrese el número de pasajeros: "))

if pasajeros <= 35:
    print("Elija el Autobús para su viaje.")
elif pasajeros <= 120:
    print("Elija el Tren para su viaje.")
else:
    print("Elija el Avión para su viaje.")