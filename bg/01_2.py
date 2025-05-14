broi_patnitsi = int(input("Моля, въведете броя пътници: "))

if broi_patnitsi <= 35:
    print("Изберете Автобус за пътуването.")
elif broi_patnitsi <= 120:
    print("Изберете Влак за пътуването.")
else:
    print("Изберете Самолет за пътуването.")