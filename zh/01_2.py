乘客数 = int(input("请输入乘客数量："))

if 乘客数 <= 35:
    print("请选择公交车进行旅行。")
elif 乘客数 <= 120:
    print("请选择火车进行旅行。")
else:
    print("请选择飞机进行旅行。")
