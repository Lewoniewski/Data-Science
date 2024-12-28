passengers = int(input("乗客数を入力してください: "))

if passengers <= 35:
    print("バスを選択してください。")
elif passengers <= 120:
    print("列車を選択してください。")
else:
    print("飛行機を選択してください。")
