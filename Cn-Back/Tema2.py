import json

import numpy as np
import scipy.linalg as la


eps = np.float_power(10, -10)


def dot_matrix(a, b):
    # Transpose
    b_t = list(zip(*b))

    # Nested list comprehension to calculate matrix multiplication
    return [
        [
            sum(el_a * el_b for el_a, el_b in zip(row_a, row_b))
            for row_b in b_t
        ] for row_a in a
    ]


def pivot_matrix(A_init):
    n = len(A_init)

    identity_matrix = [[float(i == j) for i in range(n)] for j in range(n)]

    swaps = list(range(n))
    swaps.append(0)
    for j in range(n):
        row = max(range(j, n), key=lambda i: abs(A_init[i][j]))
        if j != row:
            # Swap the rows
            identity_matrix[j], identity_matrix[row] = identity_matrix[row], identity_matrix[j]
            swaps[j], swaps[row] = swaps[row], swaps[j]
            swaps[-1] += 1

    return identity_matrix, swaps


def lu_decomposition(A_init):
    n = len(A_init)

    A = [[0.0] * n for i in range(n)]

    P, P_swaps = pivot_matrix(A_init)
    PA_init = dot_matrix(P, A_init)

    for j in range(n):
        A[j][j] = 1.0

        for i in range(j+1):
            s1 = sum(A[k][j] * A[i][k] for k in range(i))
            A[i][j] = PA_init[i][j] - s1

        for i in range(j, n):
            s2 = sum(A[k][j] * A[i][k] for k in range(j))
            if i != j:
                if np.abs(A[j][j]) < eps:
                    raise ZeroDivisionError
                A[i][j] = (PA_init[i][j] - s2) / A[j][j]

    return A, P_swaps


def det(A, P_swaps):
    n = len(A)
    prod = 1 if P_swaps % 2 == 0 else -1

    for i in range(n):
        prod *= A[i][i]
    return prod


def forward_substitution(A, b_init):
    n = len(A)
    x = []
    for i in range(n):
        x_i = (b_init[i] - sum([
            (A[i][j] if i != j else 1) * x[j]
            for j in range(i)]))  # No division, because the first diagonal is 1
        x.append(x_i)
    return x


def reverse_substitution(A, b_init):
    n = len(A)
    x = []
    for i in range(n):
        if np.abs(A[i][i]) < eps:
            raise ZeroDivisionError
        x_i = (b_init[i] - sum([
            A[i][j] * x[j]
            for j in range(i)])) / A[i][i]
        x.append(x_i)
    return x


def manual_compute_solution(A_init, b_init, display=False):
    # Descompunerea LU
    A, P_swaps = lu_decomposition(A_init)
    # print("\n".join([str(row) for row in A]))
    # print()
    # print("Det", det(A, P_swaps))
    # print()
    # P, L, U = la.lu(A_init)
    # print(L)

    y = forward_substitution(A, b_init)

    # Oglindim vertical si apoi orizontal pe A pentru a refolosi algoritmul
    # de la substitutie directa la cel de substitutie inversa
    A = list(reversed([
        list(reversed(row)) for row in A
    ]))

    x = list(reversed(reverse_substitution(A, list(reversed(y)))))

    # for row in range(n):
    #     suma = sum([A_init[row][col] * x[col] for col in range(n)])
    #     terms = [str(A_init[row][col]) + "*" + str(x[col]) for col in range(n)]
    #     print(
    #         " + ".join([str(term) for term in terms]),
    #         "=", suma,
    #         "[OK]" if suma == b_init[row] else "[Not OK]"
    #     )

    norm = la.norm(np.dot(A_init, x) - b_init)
    if display:
        print("||A_init * x - b_init||", norm, "[OK]" if norm < eps else "[Not OK]")

    return x, norm  # [x_val for _, x_val in sorted(zip(P_swaps[:-1], x), key=lambda pair: pair[0])]


def inverse(A_init):
    n = len(A_init)
    identity_matrix = [[float(i == j) for i in range(n)] for j in range(n)]
    return list(zip(*list(np.array([manual_compute_solution(A_init, col)[0] for col in identity_matrix])[[1, 0, 2]])))


def main():
    global eps
    # Date Input
    n = 3
    A_init = [
        [2.5, 2, 2],
        [5, 6, 5],
        [5, 6, 6.5]]
    b_init = [2, 2, 2]
    try:
        with open("tema2_input.json", "r") as f:
            json_input = json.loads(f.read())
            n = json_input["n"]
            A_init = json_input["A_init"]
            b_init = json_input["b_init"]
            eps_power = json_input["eps_power"]
            eps = np.float_power(10, eps_power)
    except Exception:
        print("Nu a putut fi citit fisierul de input, folosim datele default.")

    # Rezolvare
    x_LU, norm = manual_compute_solution(A_init, b_init, display=False)
    print("||A_init * x - b_init||", norm, "[OK]" if norm < eps else "[Not OK]")
    x_LU = np.array(x_LU)
    x_lib = la.lu_solve(la.lu_factor(A_init), b_init, trans=0)
    # print("[ x1 x2 x3 ] =", x_lib)

    norm = la.norm(x_LU - x_lib)
    print("||x_LU - x_lib||", "=", norm, "[OK]" if norm < eps else "[Not OK]")

    A_init_lib_inv = la.inv(A_init)
    norm = la.norm(x_LU - A_init_lib_inv.dot(b_init))
    print("||x_LU - A_lib_inv * b_init||", "=", norm, "[OK]" if norm < eps else "[Not OK]")

    A_LU_inv = inverse(A_init)
    norm = la.norm(A_LU_inv - A_init_lib_inv)
    print("||A_LU_inv - A_lib_inv||", "=", norm, "[OK]" if norm < eps else "[Not OK]")


if __name__ == '__main__':
    main()
