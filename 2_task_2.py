some_list = input("Введите список через запятую ").split(",")
for i in range(1, len(some_list), 2):
    some_list[i - 1], some_list[i] = some_list[i], some_list[i - 1]
print(','.join([str(i) for i in some_list]))
