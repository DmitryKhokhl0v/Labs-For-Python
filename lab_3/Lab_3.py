import itertools
point = 15
bag = [[0, 0, 0, 0], [0, 0, 0, 0]]
placeIndex = [0, 0, 0]
weightPoint = []
variations = [[[0, 1, 2, 3, 4, 6], [5, 7, 8, 9, 10, 11]], [[0, 1, 2, 3, 7], [4, 5, 6, 8, 9, 10, 11]],
              [[0, 1, 2, 3, 4, 8], [5, 7, 6, 9, 10, 11]], [[0, 1, 2, 3, 4, 9], [5, 7, 6, 8, 10, 11]],
              [[0, 1, 2, 3, 10], [5, 7, 6, 9, 4, 8, 11]], [[0, 1, 2, 4, 9, 8], [5, 7, 6, 3, 10, 11]],
              [[0, 1, 2, 4, 9, 8], [5, 7, 6, 3, 10, 11]], [[0, 1, 2, 3, 10], [5, 7, 6, 4, 8, 9, 11]]]
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
        if placeIndex[0] >= 4:
            placeIndex[2] = 1
            break
        if place <= 4 - placeIndex[0] and flag:
            point += this_object[3]
            flag = False
        bag[0][placeIndex[0]] = this_object[1]
        placeIndex[0] += 1
        place -= 1

    if placeIndex[2] == 1:
        if place > 0:
            if place <= 4-placeIndex[1]:
                point += this_object[3]
                for i in range(place):
                    if placeIndex[1] >= 4:
                        break
                    bag[1][placeIndex[1]] = this_object[1]
                    placeIndex[1] += 1


# ключ для сортировки
def weight_of_ob(weight):
    return weight[2]


# сортировка по ценности в очках
for i in range(12):
    weightPoint.append([i, objects[i][2], objects[i][3] / objects[i][2]])
weightPoint.sort(key=weight_of_ob, reverse=True)

for i in range(6):
    add_to_bag(objects[weightPoint[i][0]])
for i in range(6):
    point = point - objects[weightPoint[i + 6][0]][3]

print(bag[0])
bag[1].reverse()
print(bag[1])
print(f'Очки: {point}')

print('\n')
print('Дополниетельное задание')
for i in range(len(variations)):
    bag = [[0, 0, 0, 0], [0, 0, 0, 0]]
    point = 15
    placeIndex = [0, 0, 0]
    for j in range(len(variations[i][0])):
        add_to_bag(objects[weightPoint[variations[i][0][j]][0]])
    for j in range(len(variations[i][1])):
        point = point - objects[weightPoint[variations[i][1][j]][0]][3]

    if point > 0:
        print(bag[0])
        bag[1].reverse()
        print(bag[1])
        print(f'Очки: {point}\n')
