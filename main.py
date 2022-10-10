#!/usr/bin/env python3
# coding=utf-8

import random


# функция для получения массива случайных чисел
def random_array(n, m, max_value=11):
    array = []  # основной массив
    for i in range(0, n):
        sub_array = []  # подмассив с числами
        for j in range(m):
            # от минимального числа (-10) до максимального 10 с шагом (1)
            number = random.randrange(-10, max_value, 1)
            sub_array.append(number)  # добавление случайного числа в подмассив
        array.append(sub_array)  # добавление подмассива в массив
    return array  # возвращается массив с подмассивами внутри


# функция для вывода массива
def print_array(array):
    print()
    for i in array:  # перебор по подмассивам(строкам)
        for j in i:  # перебор по элементам строк
            print("%4d\t" % j, end='')
        print()


# функция для нахождения количества нулей в таблице
def counting(array):
    print()
    count = 0
    for i in range(len(array)):
        for j in range(len(array[i])):
            if array[i][j] == 0:
                count += 1
    print("Количество нулей в таблице: %d" % count)
    print()
    return count


def main():
    # вызов функции рандома массива, которая возвращает полученный массив
    array = random_array(4, 5)  # можно изменить размер
    print("Условие задания:\n"
          "Подсчитать количество нулей в таблице и\n"
          "заменить на это значение все нечетные целые элементы таблицы")
    # вызов функции вывода массива
    print_array(array)
    # вызов функции подсчета
    count = counting(array)
    while True:
        print("1. Заполнить массив случайными числами;")
        print("2. Выполнить задание;")
        print("3. Выход.")
        key = input('Введите команду (1, 2 или 3): ')
        if key == '1':
            array = random_array(4, 5)
            print_array(array)
            count = counting(array)
        elif key == '2':
            # выполнение условия
            for i in range(len(array)):
                for j in range(len(array[i])):
                    if array[i][j] < 0:
                        array[i][j] = count
            print_array(array)
            break  # выход из цикла
        elif key == '3':
            exit(0)  # выход из программы


if __name__ == '__main__':
    main()
