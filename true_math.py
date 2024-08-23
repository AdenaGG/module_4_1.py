from math import inf


def divide(first, second):
    if second == 0:
        return print('inf')
    else:
        return print(first / second)


divide(int(input('Введите число td: ')), int(input("Введите число td 2: ")))

