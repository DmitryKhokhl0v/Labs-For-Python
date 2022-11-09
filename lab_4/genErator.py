import random


def give_a_cell():
    alf = 'ABCDEFGHIJKLNMOPQRSTUVWXYZ'
    alf1 = '1234567890'
    cell = []
    cellf = ''
    while len(cell) < 3:
        arr = alf[random.randint(0, 25)]
        cell.append(str(arr))
    while len(cell) < 5:
        arr = alf1[random.randint(0, 9)]
        cell.append(arr)
        random.shuffle(cell)
    for i in cell:
        cellf += i
    return cellf



