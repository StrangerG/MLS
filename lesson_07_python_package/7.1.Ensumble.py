#!/usr/bin/python
# -*- coding:utf-8 -*-

import operator
import matplotlib.pyplot as plt


def c(n, k):
    return reduce(operator.mul, range(n-k+1, n+1)) / reduce(operator.mul, range(1, k+1))


def bagging(n, p):
    s = 0
    for i in range(n / 2 + 1, n + 1):
        s += c(n, i) * p ** i * (1 - p) ** (n - i)
    return s


if __name__ == "__main__":
    x = range(9, 100, 2)
    y = []
    for t in x:
        res = bagging(t, 0.6)
        y.append(res)
        print t, '次采样正确率：', res

    plt.plot(x, y, 'r-')
    plt.plot(x, y, '*')
    plt.grid(True)
    plt.show()
