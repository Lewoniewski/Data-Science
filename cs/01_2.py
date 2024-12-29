cestujici = int(input("Zadejte počet cestujících: "))

if cestujici <= 35:
    print("Pro cestu zvolte Autobus.")
elif cestujici <= 120:
    print("Pro cestu zvolte Vlak.")
else:
    print("Pro cestu zvolte Letadlo.")
