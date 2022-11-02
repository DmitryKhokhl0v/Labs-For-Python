point = 15
bag = [[0, 0, 0, 0], [0, 0, 0]]
placeIndex = [0, 0, 0]
weightPoint = []

objects = [['Винтовка', 'в', 3, 25], ['Пистолет', 'п', 2, 15],
           ['Боекомплект', 'б', 2, 15], ['Аптечка', 'а', 2, 20],
           ['Ингалятор', 'и', 1, 0], ['Нож', 'н', 1, 15],
           ['Топор', 'т', 3, 20], ['Оберег', 'о', 1, 25],
           ['Фляжка', 'ф', 1, 15], ['Антидот', 'д', 1, 10],
           ['Еда', 'к', 2, 20], ['Арбалет', 'р', 2, 20]]

# функция добавления предмета в рюкзак
def add_to_bag(this_object):
    global placeIndex
    global point
    place = this_object[2]
    flag = True
    for i in range(place):
        if (placeIndex[0] >= 4):
            placeIndex[2] = 1
            break
        if (place <= 4 - placeIndex[0] and flag):
            point += this_object[3]
            flag = False
        bag[0][placeIndex[0]]=this_object[1]
        placeIndex[0] += 1
        place -= 1

    if(placeIndex[2] == 1):
        if(place > 0):
            if(place <= 4-placeIndex[1]):
                point += this_object[3]
                for i in range(place):
                    if (placeIndex[1] >= 4):
                        break
                    bag[1][placeIndex[1]]=this_object[1]
                    placeIndex[1] += 1


# ключ для сортировки
def weight_of_ob(weight):
    return weight[2]


# сортировка по ценности в очках
for i in range(12):
    weightPoint.append([i, objects[i][2], objects[i][3] / objects[i][2]])
weightPoint.sort(key=weight_of_ob, reverse=True)


for i in range(5):
    if i != 4:
        add_to_bag(objects[weightPoint[i][0]])
    else:
        add_to_bag(objects[weightPoint[5][0]])
for i in range(6):
    point = point - objects[weightPoint[i + 6][0]][3]
point = point - objects[weightPoint[4][0]][3]

print(bag[0])
bag[1].append(" ")
bag[1].reverse()
print(bag[1])
print(f'point: {point}')
print('существует как минимум один вариант решения \n для случая с 7 ячейками')