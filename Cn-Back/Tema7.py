import time
import random
from itertools import repeat
from sympy import Symbol, sqrt
from concurrent.futures.process import ProcessPoolExecutor


eps = 10 ** (-9)


def f1():
    x = Symbol('x')
    f = x ** 3 - 6 * x ** 2 + 11 * x - 6

    return f.diff(x)


def f2():
    x = Symbol('x')
    f = 42 * x * x ** 4 - 55 * x ** 3 - 42 * x ** 2 + 49 * x - 6

    return f.diff(x)


def f3():
    x = Symbol('x')
    f = 8 * x ** 4 - 38 * x ** 3 + 49 * x ** 2 - 22 * x + 3

    return f.diff(x)


def f4():
    x = Symbol('x')
    f = x ** 4 - 6 * x ** 3 + 13 * x ** 2 - 12 * x + 4

    return f.diff(x)


functions = [
    "x ** 3 - 6 * x ** 2 + 11 * x - 6",
    "42 * x * x ** 4 - 55 * x ** 3 - 42 * x ** 2 + 49 * x - 6",
    "8 * x ** 4 - 38 * x ** 3 + 49 * x ** 2 - 22 * x + 3",
    "x ** 4 - 6 * x ** 3 + 13 * x ** 2 - 12 * x + 4"
]

tests = {
    "x ** 3 - 6 * x ** 2 + 11 * x - 6": [
        [1.0, -6.0, 11.0, -6.0],
        f1()
    ],
    "42 * x * x ** 4 - 55 * x ** 3 - 42 * x ** 2 + 49 * x - 6": [
        [42.0, -55.0, -42.0, 49.0, -6.0],
        f2()
    ],
    "8 * x ** 4 - 38 * x ** 3 + 49 * x ** 2 - 22 * x + 3": [
        [8.0, -38.0, 49.0, -22.0, 3.0],
        f3()
    ],
    "x ** 4 - 6 * x ** 3 + 13 * x ** 2 - 12 * x + 4": [
        [1.0, -6.0, 13.0, -12.0, 4.0],
        f4()
    ]
}


def first_derivative(a, f):
    x = Symbol('x')
    return f.evalf(subs={x: a})


def second_derivative(a, f):
    x = Symbol('x')
    f2 = f.diff(x)
    return f2.evalf(subs={x: a})


def horner(a, n, x):
    h = a[0]

    for i in range(1, n + 1):
        h = h * x + a[i]

    return h


def generate_solution(args):
    a, f = args
    k = 0
    n = 3
    A = max(a)
    R = (abs(a[0]) + A) / abs(a[0])

    x0 = random.uniform(-R, R)
    x = x0

    kmax = 1000

    while True:

        Px = horner(a, n, x)
        try:
            firstDeriv = float(first_derivative(x, f))
            secondDeriv = float(second_derivative(x, f))
        except TypeError:
            return None, None

        H = float((n - 1) ** 2 * firstDeriv ** 2 - n * (n - 1) * Px * secondDeriv)

        if H < 0:
            x0 = random.uniform(-R, R)
            x = x0

        semn = 1 if firstDeriv >= 0 else -1

        if abs(firstDeriv + semn * sqrt(H)) <= eps:
            x0 = random.uniform(-R, R)
            x = x0

        delta = n * Px / (firstDeriv + semn * sqrt(H))

        x = x - delta
        k = k + 1

        if not (k <= kmax and eps <= abs(delta) <= 10 ** 8):
            break

    return x, delta


def solve(a, f):
    runs = 50
    good_values = list()
    start_time = time.time()
    with ProcessPoolExecutor() as executor:
        for x, delta in executor.map(generate_solution, repeat([a, f], runs)):
            if x is not None:
                if abs(delta) < eps:
                    exists = False
                    for good_val in good_values:
                        if abs(float(good_val) - x) < eps:
                            exists = True
                    if not exists:
                        good_values.append(str(x))
                    # print("Found x =", x)

    # print("Good values:")
    # print("\n".join(good_values))
    # print("Time elapsed: {}s".format(time.time() - start_time))
    return good_values


if __name__ == '__main__':
    for test in tests:
        print(test)
        params = tests[test]
        output = solve(*params)
        # with open("Function_{}_output.txt".format(functions.index(test)), "w") as fd:
        #     fd.write("\n".join(output))
        print("----------------------------------------------")
