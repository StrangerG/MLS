#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
import numpy as np
import matplotlib.pyplot as plt


def calc(data):
    n = len(data)
    miu = 0.0
    miu2 = 0.0
    miu3 = 0.0

    for x in data:
        miu += x
        miu2 += x ** 2
        miu3 += x ** 3
    miu /= n
    miu2 /= n
    miu3 /= n
    sigma = math.sqrt(miu2 - miu * miu)
    return [miu, sigma, miu3]

def calc_stat(data):
    [miu, sigma, miu3] = calc(data)
    n = len(data)
    miu4 = 0.0

    for x in data:
        x -= miu
        miu4 += x ** 4
    miu4 /= n

    skew = (miu3 - 3 * miu * sigma ** 2 - miu ** 3) / (sigma ** 3)
    kurt = miu4 / (sigma ** 4)
    return [miu, sigma, skew, kurt]


if __name__ == "__main__":
    data = list(np.random.randn(10000))
    data2 = list(2 * np.random.randn(10000))
    data3 = [x for x in data if x > -0.5]
    data4 = list(np.random.uniform(0, 4, 10000))
    [miu, sigma, skew, kurt] = calc_stat(data)
    [miu2, sigma2, skew2, kurt2] = calc_stat(data2)
    [miu3, sigma3, skew3, kurt3] = calc_stat(data3)
    [miu4, sigma4, skew4, kurt4] = calc_stat(data4)

    print miu, sigma, skew, kurt
    print miu2, sigma2, skew2, kurt2
    print miu3, sigma3, skew3, kurt3
    print miu4, sigma4, skew4, kurt4

    info = r'$\mu=%.2f,\ \sigma=%.2f\ skew=%.2f,\ kurt=%.2f$'\
            % (miu, sigma, skew, kurt)
    info2 = r'$\mu=%.2f,\ \sigma=%.2f\ skew=%.2f,\ kurt=%.2f$'\
            % (miu2, sigma2, skew2, kurt2)

    plt.text(1, 0.38, info, bbox=dict(facecolor='red', alpha=0.25))
    plt.text(1, 0.35, info2, bbox=dict(facecolor='green', alpha=0.25))
    plt.hist(data, 50, normed=True, facecolor='r', alpha=0.9)
    plt.hist(data2, 80, normed=True, facecolor='g', alpha=0.8)
    plt.grid(True)
    plt.show()

