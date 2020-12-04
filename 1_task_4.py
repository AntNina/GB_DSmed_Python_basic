n = abs(int(input("Введите целое положительное число ")))
mx = n % 10
while n > 0:
    n = n // 10
    if n % 10 > mx:
        mx = n % 10
    if n > 9:
        continue
    else:
        print("Самая большая цифра в числе ", mx)
        break
