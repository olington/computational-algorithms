from math import cos

def f(x):
    return x*x
    

def interpolate(x, y, x_value):
    n = len(x)
    i_near = min(range(n), key = lambda i: abs(x[i] - x_value))

    h = [0 if not i else x[i] - x[i - 1] for i in range(n)]
    
    A = [0 if i < 2 else h[i-1] for i in range(n)]
    B = [0 if i < 2 else -2 * (h[i - 1] + h[i]) for i in range(n)]
    D = [0 if i < 2 else h[i] for i in range(n)]
    F = [0 if i < 2 else -3 * ((y[i] - y[i - 1]) / h[i] - (y[i - 1] - y[i - 2]) / h[i - 1]) for i in range(n)]

    ksi = [0 for i in range(n + 1)]
    eta = [0 for i in range(n + 1)]
    for i in range(2, n):
        ksi[i + 1] = D[i] / (B[i] - A[i] * ksi[i])
        eta[i + 1] = (A[i] * eta[i] + F[i]) / (B[i] - A[i] * ksi[i])

    c = [0 for i in range(n + 1)]
    for i in range(n - 2, -1, -1):
        c[i] = ksi[i + 1] * c[i + 1] + eta[i + 1]

    a = [0 if i < 1 else y[i-1] for i in range(n)]
    b = [0 if i < 1 else (y[i] - y[i - 1]) / h[i] - h[i] / 3 * (c[i + 1] + 2 * c[i]) for i in range(n)]
    d = [0 if i < 1 else (c[i + 1] - c[i]) / (3 * h[i]) for i in range(n)]

    return a[i_near] + b[i_near] * (x_value - x[i_near - 1]) + c[i_near] * ((x_value - x[i_near - 1]) ** 2) + d[i_near] * ((x_value - x[i_near - 1]) ** 3)


def create_table(x_start, step, num):
    x_tbl = [x_start + step * i for i in range(num)]
    y_tbl = [f(x) for x in x_tbl]
    return x_tbl, y_tbl


def print_table(x, y):
    print("   x   ", " y   ")
    for i in range(len(x)):
        print("%.4f %.4f" % (x[i], y[i]))
    print()

     
x_start = float(input("Input x start: "))
x_step = float(input("Input step for x value: "))
num = int(input("Input number of dots: "))

x_tbl, y_tbl = create_table(x_start, x_step, num)
print("\nTable:")
print_table(x_tbl, y_tbl)

x = float(input("Input x: "))

p = interpolate(x_tbl, y_tbl, x)
print("\nInterpolated: ", p)
print("F(x) : ", f(x))
print("Error  : ", abs(f(x) - p), "\n")
