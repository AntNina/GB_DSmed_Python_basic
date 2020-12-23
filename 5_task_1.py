file_1 = open('text_1.txt', 'w', encoding='utf-8')

line = input('Введите текст ')
while line:
    file_1.writelines(line + '\n')
    line = input('Введите текст ')
    if not line:
        break

file_1.close()
