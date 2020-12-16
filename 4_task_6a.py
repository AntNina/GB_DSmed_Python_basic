from itertools import count

for el in count(int(input('Введите стартовое число '))):
    if el > 1500:
        break
    else:
        print(el)
