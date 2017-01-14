# -*- coding:utf-8 -*-

# sigular, left eigenvector, right eigenvector
def restore(sigma, u, v, k):
    print k
    m = len(u)
    n = len(v[0])
    a = np.zeros((m, n))
    for k in range(k + 1):
        for i in range(m):
            a[i] += sigma[k] * u[i][k] * v[k]
    b = a.astype('uint8')
    Image.fromarray(b).save("svd_" + str(k) + ".png")
