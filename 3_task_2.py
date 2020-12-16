def my_func(name, surname, year, city, email, telephone):
    return ' '.join([name, surname, year, city, email, telephone])


print(my_func(surname='Иванов', name='Иван', year='1990', city='Москва', email='mail@mail.ru',
              telephone='+11111111111111'))
