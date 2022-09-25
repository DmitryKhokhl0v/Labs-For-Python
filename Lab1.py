import csv
import random


def sortf(e):
    return int(e[:2])


# Выбор 20 случайных записей, без повторений
base = []
FullbaseF = set()
while len(base) < 20:
    a = random.randint(1, 9409)
    if not(a in base):
        base.append(a)
base.sort()

nams = 1
NumOfBooks = 0
LongNamingBooks = 0
Tags = set()
flag = 0
search = input('Искать по автору (до 150 руб): ').lower()
f = open('result.txt', 'w')
with open('books.csv', 'r') as csvfile:
    table = csv.reader(csvfile, delimiter=';')
    for row in list(table)[1:]:

        Tags.update((row[12][1:].split('# ')))

        # Подсчет общего количесва книг / текущая книга
        NumOfBooks += 1

        # Подсчет подсчет книг с названием более тридцати символов
        if len(row[1]) > 30:
            LongNamingBooks += 1

        # Поиск по автору, с учётом стоимости (<150)
        lower_case = row[3].lower()
        if search in lower_case:
            if float(row[7]) < 150.00:
                print(row[1] + '. ' + row[3] + '. ' + row[7] + ' Руб.')
                flag = 1

        # Создание библеографического списка
        if len(base) > 0 and NumOfBooks == base[0]:
            f.write(str(nams) + '. ' + row[4] + '. ' + row[1] + ' - ' + row[6][6:10] + '\n')
            base.pop(0)
            nams += 1

        FullbaseF.add(row[8] + ' ' + row[1])

    if flag == 0:
        print('Поиск не дал результатов. \n')
    else:
        print('Поиск окончен. \n')

    print(f'Общее число записей: {NumOfBooks}')
    print(f'Чилсо записей с "названием" больше 30 символов: {LongNamingBooks}')

    print('Двадцать наиболее популярных книг:')
    Fullbase = list(FullbaseF)
    Fullbase.sort(key=sortf)
    for el in Fullbase[-20:]:
        print(el[2:])

    print(f'Облако тэгов: {Tags} \n')

f.close()
input()
