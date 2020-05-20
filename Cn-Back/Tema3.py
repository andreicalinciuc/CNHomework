import json
import time
import scipy.linalg as la
from copy import deepcopy


EPS = pow(10, -8)


def matrix_addition(a, b):
    sum = deepcopy(a)

    for line_nr in b:
        line = b[line_nr]
        for elem_nr in line:
            value = line[elem_nr]
            if line_nr not in sum:
                sum[line_nr] = {}
            if elem_nr not in sum[line_nr]:
                sum[line_nr][elem_nr] = .0
            sum[line_nr][elem_nr] += value

    return sum


def matrix_dot(a, b, n):
    dot = {}

    count = 0
    b_columns = [column for column in range(n) if any([column in b[row] for row in b])]
    start_time = time.time()
    for result_line in a:
        a_line = a[result_line]
        for result_column in b_columns:
            # result matrix value to be calculated: dot[result_line][result_column]
            value = .0
            for index in list(set(a_line.keys()) & set(b.keys())):
                a_val = a_line.get(index, 0)
                if not a_val:
                    continue
                b_row = b.get(index, {})
                if not b_row:
                    continue
                b_val = b_row.get(result_column, 0)
                if not b_val:
                    continue
                value += a_val * b_val
            if value:
                if result_line not in dot:
                    dot[result_line] = {}
                if result_column not in dot[result_line]:
                    dot[result_line][result_column] = value
        count += 1
        if count % 50 == 0:
            print("Estimated time left: {}s".format(int(
                (len(a) - count) *
                (time.time()-start_time) / 50)))
            start_time = time.time()

    return dot


def load_matrix_from_string(string, ignore_max_len_limit=False):
    matrix = {}
    lines = string.splitlines()
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


def load_matrix_from_file(path, ignore_max_len_limit=False):
    with open(path, "r") as f:
        content = f.read()
    return load_matrix_from_string(content, ignore_max_len_limit)


def check_equal_matrix(a, b, n):
    for line_nr in range(n):
        line_a = a.get(line_nr)
        line_b = b.get(line_nr)
        if line_a is None and line_b is None:
            continue
        elif (line_a is None or line_b is None) and line_a != line_b:
            return False
        else:
            for row_nr in range(n):
                cell_a = line_a.get(row_nr)
                cell_b = line_b.get(row_nr)
                if cell_a is None and cell_b is None:
                    continue
                elif (cell_a is None or cell_b is None) and cell_a != cell_b:
                    return False
                elif abs(cell_a - cell_b) < EPS:
                    continue
                else:
                    return False
    return True


def main():
    a, a_size = load_matrix_from_file("Tema3_input/a.txt")
    b, b_size = load_matrix_from_file("Tema3_input/b.txt")
    a_plus_b, a_plus_b_size = load_matrix_from_file("Tema3_input/aplusb.txt", ignore_max_len_limit=True)
    a_ori_b, a_ori_b_size = load_matrix_from_file("Tema3_input/aorib.txt", ignore_max_len_limit=True)

    a_plus_b_calculated = matrix_addition(a, b)
    if check_equal_matrix(a_plus_b, a_plus_b_calculated, a_plus_b_size):
        print("A + B is OK(error < Epsilon)")
    else:
        print("A + B is not OK (error > Epsilon)")

    a_ori_b_calculated = matrix_dot(a, b, a_size)
    if check_equal_matrix(a_ori_b, a_ori_b_calculated, a_ori_b_size):
        print("A * B is OK (error < Epsilon)")
    else:
        print("A * B is not OK (error > Epsilon)")


if __name__ == '__main__':
    main()
