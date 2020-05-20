import numpy as np
import random
import math


tests = {
    "x ** 4 - 12 * x ** 3 + 30 * x ** 2 + 12":
        (1, 5, lambda x: x ** 4 - 12 * x ** 3 + 30 * x ** 2 + 12),
    "math.sin(x) - math.cos(x)":
        (0, 31 * np.pi / 16, lambda x: math.sin(x) - math.cos(x)),
    "math.sin(2 * x) + math.sin(x) + math.cos(3 * x)":
        (0, 31 * np.pi / 16, lambda x: math.sin(2 * x) + math.sin(x) + math.cos(3 * x)),
    "math.sin(x) ** 2 - math.cos(x) ** 2":
        (0, 63 * np.pi / 32, lambda x: math.sin(x) ** 2 - math.cos(x) ** 2)
}


def gen_x(x_0, x_n, n):
    x = [x_0, x_n]
    for i in range(n-1):
        new_x = random.uniform(x_0, x_n)
        while new_x in x:
            new_x = random.uniform(x_0, x_n)
        x.append(new_x)
    return list(sorted(x))


def five_squares(x_0, x_n, func):
    m = 4
    n = 4

    x = gen_x(x_0=x_0, x_n=x_n, n=n)

    B = []
    f = []
    for i in range(m + 1):
        B.append([])
        for j in range(m + 1):
            sum = 0
            for k in range(n + 1):
                sum += x[k] ** (i + j)
            B[i].append(sum)

        sum = 0
        for k in range(n + 1):
            sum += func(x[k]) * (x[k] ** i)
        f.append(sum)

    a = np.linalg.solve(np.array(B), np.array(f))
    a = np.array(list(reversed(a)))

    x_t = random.uniform(x_0, x_n)

    Sm = a[0]
    for i in range(1, m + 1):
        Sm = Sm * x_t + a[i]

    print("Metoda: 5 patrate")
    print("\tx = {}".format(x_t))
    print("\tSm = {}".format(Sm))
    print("\tf(x) = {}".format(func(x_t)))
    print("\t|Sm(x) - f(x)| = {}".format(abs(Sm - func(x_t))))


def interpolation(x_0, x_n, func):
    m = 7
    n = 2 * m

    p = 2 * math.pi

    if x_n < p:
        x = gen_x(x_0, x_n, n)
        T = []

        for i in range(n + 1):
            T.append([])

            for j in range(n + 1):
                if j == 0:
                    T[i].append(1)
                elif j % 2 != 0:
                    T[i].append(math.sin((j + 1) / 2 * x[i]))
                else:
                    T[i].append(math.cos(j / 2 * x[i]))

        Y = [func(x[i]) for i in range(n+1)]

        x_t = random.uniform(0, p - 0.1)
        Tn = Y[0]
        for k in range(1, n + 1, 2):
            Tn += Y[k] * math.sin((k + 1) / 2 * x_t) + Y[k + 1] * math.cos(k / 2 * x_t)

        print("Method: Interpolare trigonometrica")
        print("\tx = {}".format(x_t))
        print("\tTn = {}".format(Tn))
        print("\tf(x) = {}".format(func(x_t)))
        print("\t|Tn(x) - f(x)| = {}".format(abs(Tn - func(x_t))))


def main():
    for test in tests:
        params = tests[test]
        print("Function: {}".format(test))
        five_squares(*params)
        interpolation(*params)
        print("-----------------------------------------------\n")


if __name__ == '__main__':
    main()
