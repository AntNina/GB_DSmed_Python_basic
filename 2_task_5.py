rating = [8, 6, 4, 2, 1]
while True:
    rating.append(int(input('Введите новый рейтинг: ')))
    rating.sort()
    rating.reverse()
    print(rating)
