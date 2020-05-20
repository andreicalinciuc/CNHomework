import numpy as np
import scipy.linalg as la
from copy import deepcopy


PRECISION = 8
EPS = pow(10, -PRECISION)


def load_matrix_from_file(path, ignore_max_len_limit=False):
    matrix = {}
    with open(path, "r") as f:
        lines = f.read().splitlines()
        matrix_size = int(lines[0])
    for line in lines[1:]:
        if not line:
            continue
        value, node_from, node_to = line.split(", ")
        value, node_from, node_to = float(value), int(node_from), int(node_to)
        if node_from not in matrix:
            matrix[node_from] = {}
        if node_to not in matrix[node_from]:
            matrix[node_from][node_to] = .0
        matrix[node_from][node_to] += value
    if not ignore_max_len_limit:
        for line_nr in matrix:
            if len(matrix[line_nr]) > 10:
                print("Linia {} contine mai mult de 10 elemente nenule!  [{}]".format(line_nr, ", ".join([str(elem) for elem in matrix[line_nr]])))
    return matrix, matrix_size


def load_vector_from_file(path):
    with open(path, "r") as f:
        lines = f.read().splitlines()
        vector_size = int(lines[0])
    vector = [float(line) for line in lines[1:] if line]
    if len(vector) != vector_size:
        raise Exception("Vector length declared not equal to actual length!")
    return vector, vector_size


def check_diagonal(a, n):
    for index in range(n):
        try:
            if a[index][index] < EPS:
                return False
        except IndexError:
            return False
    return True


def solve(a, b, n, w=1):
    x_1 = [0] * n
    norm = 1

    for k in range(10000):
        x_2 = deepcopy(x_1)
        for line_nr in a.keys():
            line = a[line_nr]
            s1 = sum([line[col_nr] * x_1[col_nr] for col_nr in line.keys() if col_nr < line_nr])
            s2 = sum([line[col_nr] * x_2[col_nr] for col_nr in line.keys() if col_nr > line_nr])

            x_1[line_nr] = (1-w) * x_2[line_nr] + (
                    (w/a[line_nr][line_nr]) *
                    (b[line_nr] - s1 - s2)
            )

        norm = la.norm(np.array(x_1) - np.array(x_2))
        if abs(norm) < EPS:
            break

    if abs(norm) < EPS:
        return [round(elem, PRECISION) for elem in x_1]
    else:
        return None


def main():
    for a_nr in range(5):
        a, n = load_matrix_from_file("Tema4_input/a_{}.txt".format(a_nr+1), ignore_max_len_limit=True)
        b, n = load_vector_from_file("Tema4_input/b_{}.txt".format(a_nr+1))

        print()
        if check_diagonal(a, n):
            print("#{} Diagonal: No null values".format(a_nr+1))
            x = solve(a, b, n)
            print("#{} Solution: {}".format(a_nr+1, x if x else "Cannot compute"))
        else:
            print("#{} Diagonal: Contains null values".format(a_nr+1))
            print("#{} Solution: Cannot compute".format(a_nr+1))


if __name__ == '__main__':
    main()
