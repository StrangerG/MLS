# -*- coding:utf-8 -*-

def whitening(x):
    m = len(x)
    n = len(x[0])

    # calc x * x'
    xx = [[0.0] * n for tt in range(n)]
    for i in range(n):
        for j in range(i, n):
            s = 0.0
            for k in range(m):
                s += x[k][i] * x[k][j]
            xx[i][j] = s
            xx[j][i] = s

    # calc the eigenvalue and eigenvector of x * x'
    lamda, egs = np.linalg.eig(xx)
    lamda = [1 / math.sqrt(d) for d in lamda]

    # calc whiten matrix: U'*D^(-0.5)*U
    t = [[0.0] * n for tt in range(n)]
    for i in range(n):
        for j in range(n):
            t[i][j] = lamda[j] * egs[i][j]
    whiten_matrix = [[0.0] * n for tt in range(n)]
    for i in range(n):
        for j in range(n):
            s = 0.0
            for k in range(n):
                s += t[i][k] * egs[j][k]
            whiten_matrix[i][j] = s

    # whiten x
    wx = [0.0] * n
    for j in range(m):
        for i in range(n):
            s = 0.0
            for k in range(n):
                s += whiten_matrix[i][k] * x[j][k]
            wx[i] = s
        x[j] = wx[:]
