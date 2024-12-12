passageiros = int(input("Digite o número de passageiros: "))

if passageiros <= 35:
    print("Escolha o Ônibus para a viagem.")
elif passageiros <= 120:
    print("Escolha o Trem para a viagem.")
else:
    print("Escolha o Avião para a viagem.")