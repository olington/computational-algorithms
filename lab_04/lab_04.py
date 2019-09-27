import matplotlib.pyplot as plt
import numpy as np


def calculate_rms(x, y, p, n):
    sum_x_n = []
    t = 0
    for j in range (n * 2 - 1):
        for i in range (len(x)):
            t += x[i] ** j * p[i]
        sum_x_n.append(t)
        t = 0
    
    sum_y_x_n = []
    t = 0
    for j in range (n):
        for i in range (len(x)):
            t += x[i] ** j * p[i] * y[i]
        sum_y_x_n.append(t)
        t = 0
    
    mtrx = []
    for i in range(n):
        mtrx.append(sum_x_n[i:i + n])
    
    for i in range(n):
        mtrx[i].append(sum_y_x_n[i])
    
    for i in mtrx:
        print(i)
    
    a = Gauss(mtrx)
    return a


def Gauss(mtr):
    l = len(mtr)
    # приводим к треугольному виду
    for k in range(l):
        for i in range(k + 1, l):
            t = - (mtr[i][k] / mtr[k][k])
            for j in range(k, l + 1):
                mtr[i][j] += t * mtr[k][j]

    c = [0 for i in range(l)] # искомые коэффициенты

    for i in range(l - 1, -1, -1):
        for j in range(l - 1, i, -1):
            mtr[i][l] -= c[j] * mtr[i][j]
            c[i] = mtr[i][l] / mtr[i][i]
    return c


def show(a):
    t = np.arange(-1.0, 5.0, 0.02)
    plt.figure(1)
    plt.ylabel("y")
    plt.xlabel("x")
    res = np.zeros(len(t))
    for i in range(len(a)):
        res += a[i] * (t ** i)
    plt.plot(t, res, 'k')
    for i in range(len(x)):
        plt.plot(x[i], y[i], 'ro')
    plt.show()


def print_table(x, y, weight):
    print("x      y      weight")
    for i in range(len(x)):
        print("%.4f %.4f %.4f" % (x[i], y[i], weight[i]))
    
    print()


f = open("dots.txt", "r")
x, y, weight = [], [], []
for arr in f:
    arr = arr.split(" ")
    x.append(float(arr[0]))
    y.append(float(arr[1]))
    weight.append(float(arr[2]))

n = 0
length = len(x)
print("x    y    p")
print_table(x, y, weight)
a = calculate_rms(x, y, weight, n + 1)

print("\na:", a)

show(a)
