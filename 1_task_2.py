time = int(input("Введите время в секундах "))
hh = time // 3600
mm = (time - hh * 3600) // 60
ss = time - (hh * 3600 + mm * 60)
print(f"Время {hh:02}:{mm:02}:{ss:02}")
