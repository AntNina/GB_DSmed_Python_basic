def my_func(a, b):
    try:
        c = a / b
        return c
    except ZeroDivisionError:
        return "b не может быть ноль"


print(my_func(int(input("Введите число a = ")), int(input("Введите число b = "))))
