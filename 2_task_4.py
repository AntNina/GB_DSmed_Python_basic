some_words = input('Введите несколько слов: ').split(' ')
for i in range(len(some_words)):
    print(f'{i+1}.', (some_words[i])[:10:])
