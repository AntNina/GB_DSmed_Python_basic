from itertools import cycle

c = 0
for el in cycle([True, 'ABC', 123, None]):
    if c > 100:
        break
    print(el)
    c += 1
