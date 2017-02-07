#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import math
from time import time


def first_digit_1(number):
    while number / 10:
        number /= 10
    return number

def first_digit_2(number, a):
    number /= a
    while number / 10:
        number /= 10
        a *= 10
    return number, a

def first_digit_3(number, N3):
    # just keep the top digits if current number get bigger than N3
    while number >= N3:
        number /= 10

    n = number # keep this "simplified" number
    while number >= 10:
        number /= 10
    return n, number

def first_digit_4(number):
    number -= int(number)
    return int(10 ** number)

def first_digit_5(number):
    number -= int(number)
    frequency[int(10 ** number) - 1] += 1


if __name__ == "__main__":
    N = 1000000
    x = range(1, N + 1)
    frequency = np.zeros(9, dtype=np.int)

    f = 1 # 0! = 1
    print 'Start calculating...'
    t0 = time()

    # Alg 1
    """
    for i in x:
        f *= i # doing factorial
        n = first_digit_1(f)
        frequency[n - 1] += 1
    """

    # Alg 2
    """
    a = 1 # a is the decimal base of (f-1)
    for i in x:
        f *= i
        n, a = first_digit_2(f, a)
        frequency[n - 1] += 1
    """

    # Alg 3
    """
    N3 = N ** 3 # set (N ** 3) as the threashold
    for i in x:
        f *= i
        f, n = first_digit_3(f, N3)
        frequency[n - 1] += 1
    """

    # Alg 4 (with math thinking)
    # factorial = (a + b) * 10 ** n
    # => log(factorial) = log(a + b) + n
    """
    f = 0 # f is the logarithm of current factorial
    for i in x:
        f += math.log10(i)
        frequency[first_digit_4(f) - 1] += 1
    """

    # this is the abbreviation of Alg 4 using numpy
    """
    y = np.cumsum(np.log10(x))
    for i in y:
        frequency[first_digit_4(i) - 1] += 1
    """

    # this is the further abbreviation of Alg 4 using map as well
    y = np.cumsum(np.log10(x))
    map(first_digit_5, y) # first argument of map is a callback function

    # Finish calculating
    print frequency
    t1 = time()
    print 'Elapsed time = {}'.format(t1 - t0)

    x_axis = np.arange(1, 10)
    plt.plot(x_axis, frequency, 'r-', linewidth=2)
    plt.plot(x_axis, frequency, 'go', markersize=8)
    plt.grid(True)
    plt.show()
