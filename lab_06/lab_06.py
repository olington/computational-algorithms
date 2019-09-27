from math import e, log

a0, a1, a2 = 1, 2, 3

x_start = 0
x_step = 1
x_n = 11


# y
def f(x):
    return (a0 * x) / (a1 + a2 * x)


# y'
def f_det(x):
    return (a0 * (a1 + a2 * x) - a0 * a2 * x) / ((a1 + a2 * x) ** 2)


def getTable(start, step, amount):
    x_tbl = [start + step * i for i in range(amount)]
    y_tbl = [f(x) for x in x_tbl]
    return x_tbl, y_tbl


# односторонняя разность
def leftSideDifference(y, h):
    return [None if not i else ((y[i] - y[i - 1]) / h) for i in range(len(y))]


# центральная разность
def centerDifference(y, h):
    return [None if not i or i == len(y) - 1 else (y[i + 1] - y[i - 1]) / (2 * h) for i in range(len(y))]


def edgeAccurate(y, h):
    n = len(y)
    a = [None for i in range(n)]
    a[0] = (-3 * y[0] + 4 * y[1] - y[2]) / (2 * h)
    a[n - 1] = (y[n - 3] - 4 * y[n - 2] + 3 * y[n - 1]) / (2 * h)
    return a


def leftSideRunge(y, h):
    n = len(y)
    p = 1
    yh = leftSideDifference(y, h)
    y2h = [0 if i < 2 else (y[i] - y[i - 2]) / (2 * h) for i in range(0, n)]
    return [None if i < 2 else (yh[i] + (yh[i] - y2h[i]) / (2 ** p - 1)) for i in range(0, n)]


def centerRunge(y, h):
    n = len(y)
    p = 2
    r = 2
    ksi_h = [(y[i + 1] - y[i - 1]) / (2 * h) for i in range(2, n - 2)]
    ksi_rh = [(y[i + r] - y[i - r]) / (2 * h * r) for i in range(2, n - 2)]
    return [None if i >= n - 4 or i < 0 else (ksi_h[i] + (ksi_h[i] - ksi_rh[i]) / (r ** p - 1)) for i in range(-2, n - 2)]


# выравнивающие переменные
# производная эта по кси
def etaksi():
    return a1 / a0

# производная эта по у
def etay(y):
    return y * y

# производная кси по х
def ksix(x):
    return 1 / (x * x)

def Lining(x, y):
    return [None if x[i] == 0 else etaksi() * etууay(y[i]) * ksix(x[i]) for i in range(len(x))]


def solvedLine(text, res):
    print("-" * 164)
    print("{:<20}|".format(text), end="")
    for i in res:
        if (i != None):
            print("   {: <8.5f} |".format(i), end="")
        else:
            print("   {: <8} |".format("   -"), end="")
    print()


x, y = getTable(x_start, x_step, x_n)


solvedLine("X", x)

solvedLine("Y", y)

solvedLine("Y'", [f_det(i) for i in x])

solvedLine("Left side", leftSideDifference(y, x_step))

solvedLine("Center differences", centerDifference(y, x_step))

solvedLine("Edges accurate", edgeAccurate(y, x_step))

solvedLine("Runge left side", leftSideRunge(y, x_step))

solvedLine("Runge center", centerRunge(y, x_step))

solvedLine("Lining", Lining(x, y))
