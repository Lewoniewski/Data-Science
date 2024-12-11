pasazhyry = int(input("Введіть кількість пасажирів: "))

if pasazhyry <= 35:
    print("Виберіть Автобус для подорожі.")
elif pasazhyry <= 120:
    print("Виберіть Поїзд для подорожі.")
else:
    print("Виберіть Літак для подорожі.")