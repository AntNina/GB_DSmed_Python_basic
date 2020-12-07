pro = float(input("Введите выручку "))
cos = float(input("Введите издержки "))
if pro > cos:
    print(f"Фирма работает с прибылью. Рентабельность {pro / cos:.2f}")
    emp = int(input("Введите количество сотрудников "))
    print(f"Прибыль в расчете на одного сторудника {(pro - cos) / emp:.2f}")
elif pro == cos:
    print("Фирма работает в ноль")
else:
    print("Фирма работает в убыток")
