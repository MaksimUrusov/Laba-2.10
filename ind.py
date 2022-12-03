#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Вариант 18
Напишите функцию, находящую сумму положительных аргументов, расположенных до максимального аргумента.
"""

def max(*args):
    k = 0
    sum = 0
    if args:
        for i in args:
            if i > k:
                k = i
        for i in args:
            if i != k and i > 0:
                sum = sum + i
            else:
                break
        return 'Сумма положительных чисел до максимального - ' + str(sum)
    else:
        return None


if __name__ == "__main__":
    print(max(100, 200, 300, 5, 15, 555, 500))
