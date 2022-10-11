import csv
from time import sleep
from os import system


def esc(code):
    return f'\u001b[{code}m'


def flag_fr():
    for i in range(6):
        print(BLUE + '  ' * 4 + WHITE + '  ' * 4 + RED + '  ' * 4 + END)


def uzor(a1, b1):
    for i in range(a1):
        if i % 2 == 0:
            print((BLACK + ' ' * 2 + WHITE + ' ' * 2) * b1 + END)
        else:
            print((WHITE + ' ' * 2 + BLACK + ' ' * 2) * b1 + END)


def anim(ch):
    if ch % 2 == 0:
        print(BLUE + '  ' + WHITE + ' ' * 10 + BLUE + ' ' + END)
        print(WHITE + ' ' * 4 + BLUE + '  ' + WHITE + ' ' * 4 + BLUE + '  ' + WHITE + ' ' + END)
        print(BLUE + ' ' + WHITE + ' ' * 11 + END)
        print(BLUE + '  ' + WHITE + ' ' + BLUE + ' ' * 8 + END)
        print(BLUE + '  ' + WHITE + ' ' + BLUE + ' ' + WHITE + ' ' + BLUE + ' ' + WHITE + ' ' + BLUE + ' ' + WHITE + ' ' + BLUE + '  ' + END)
        print(BLUE + '  ' + WHITE + ' ' * 7 + BLUE + '  ' + END)
    else:
        print(BLUE + '  ' + WHITE + ' ' * 10 + BLUE + ' ' + END)
        print(WHITE + ' ' * 4 + BLUE + '  ' + WHITE + ' ' * 4 + BLUE + '  ' + WHITE + ' ' + END)
        print(BLUE + ' ' + WHITE + ' ' * 11 + END)
        print(BLUE + '  ' + WHITE + ' ' + BLUE + ' ' + WHITE + ' ' + BLUE + ' ' + WHITE + ' ' + BLUE + ' ' + WHITE + ' ' + BLUE + '  ' + END)
        print(BLUE + '  ' + WHITE + ' ' * 7 + BLUE + '  ' + END)
        print(BLUE + ' ' * 11 + END)


def array_init(array_in, st):
    for i in range(10):
        for j in range(10):
            if j == 0:
                array_in[i][j] = int(round(st * (9 - i), 1))
            if i == 9:
                array_in[i][j] = round(j, 1)
    return array_in


def array_fill(array_fi, res, st):
    for i in range(9):
        for k in range(10):
            if abs(array_fi[i][0] - res[9 - k]) < st:
                for j in range(9):
                    if 8 - j == k:
                        array_fi[i][j + 1] = 1
    return array_fi


def print_plot(plot):
    for i in range(9):
        line = ''
        for j in range(10):
            if j == 0:
                if len(str(plot[i][j])) == 2:
                    line += WHITE + str(plot[i][j])
                else:
                    line += WHITE + str(plot[i][j]) + ' '
            if plot[i][j] == 0:
                line += '  '
            elif plot[i][j] == 1:
                line += RED + '  ' + WHITE
        line += END
        print(line)
    print(WHITE + '0 1 2 3 4 5 6 7 8 9 ' + END)


RED = esc(41)
BLUE = esc(44)
WHITE = esc(47)
BLACK = esc(48)
END = esc(0)

After = 0
Before = 0

array_plot = [[0 for col in range(10)] for row in range(10)]
result = [0 for i in range(10)]

# Флаг Франции
flag_fr()
print('\n' * 2)
sleep(0.5)


# Узор 10*10
a = 10
b = 10
uzor(a, b)
print('\n' * 2)
sleep(0.5)


# График
for i in range(10):
    result[i] = i ** 2

step = round(abs((result[9] - result[0])) / 9, 1)
array_init(array_plot, step)
array_fill(array_plot, result, step)
print_plot(array_plot)
sleep(0.5)

# Cчтитывание данных
with open('books.csv', 'r') as csvfile:
    table = csv.reader(csvfile, delimiter=';')
    for row in list(table)[1:]:
        book = int(row[6][:4])
        if book > 2014:
            After += 1
        else:
            Before += 1

AllL = After + Before
Before = Before / AllL
After = After / AllL
print('\n' * 2)

# Диограмма
print('До 2014                 После 2014')
print(RED + ' ' * int(Before * 50) + str(round(Before * 100, 2)) + '%' + ' ' * int(Before * 50) + BLUE + ' ' * int(After * 50) + str(round(After * 100, 2)) + '%' + ' ' * int(After * 50) + END)
sleep(0.7)

# Анимация
print('\n\n\n Анимация (ожидание ввода)')
input()

sleep(0.7)

system('cls')

for cad in range(100):

    anim(cad)
    sleep(0.2)
    system('cls')
