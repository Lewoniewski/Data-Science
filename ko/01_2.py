passenger_count = int(input("승객 수를 입력하세요: "))

if passenger_count <= 35:
    print("여행을 위해 버스를 선택하세요.")
elif passenger_count <= 120:
    print("여행을 위해 기차를 선택하세요.")
else:
    print("여행을 위해 비행기를 선택하세요.")
