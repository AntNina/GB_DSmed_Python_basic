products, order = [], 1

continue_to_ask = True
while continue_to_ask:
    title = input('Введите название товара: ')
    price = input('Введите стоимость товара: ')
    amount = input('Введите количество: ')
    unit = input('Введите единицы измерения: ')
    products.append((order, {'title': title, 'price': price, 'amount': amount, 'unit': unit}))
    order += 1
    print(products)
    q = input('Формирование списка завершено? (yes/no)) ')
    if q == 'yes':
        continue_to_ask = False
        
analytics = {'title': [], 'price': [], 'amount': [], 'unit': []}

for _, item in products:
    analytics['title'].append(item['title'])
    analytics['price'].append(item['price'])
    analytics['amount'].append(item['amount'])
    analytics['unit'].append(item['unit'])

analytics['title'] = list(set(analytics['title']))
analytics['price'] = list(set(analytics['price']))
analytics['amount'] = list(set(analytics['amount']))
analytics['unit'] = list(set(analytics['unit']))

print(analytics)
