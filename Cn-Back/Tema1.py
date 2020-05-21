import math


def problema1():
    index = -1
    while 1 + pow(10, index * (-1)) != 1:
        index += 1

        if 1 + pow(10, index * (-1)) == 1:
            return index


def problema2(real=True):
    x = 1.0
    u = problema1()
    y = u
    z = u
    #(1.0, 31.000001015419347, 31.000001015419347)

    if not real:
        return (1.0, 31.000001015419347, 31.000001015419347)

    while (x + y) + z == x + (y + z):
        y = y + 0.000001
        z = z + 0.000001
        print(y)
        if (x + y) + z != x + (y + z):
            return (x, y, z)


def divideA(mat1, n):
    lst = []
    m = int(math.log2(n))
    p = int(n / m)
    for i in range(0, p):
        mat = []
        for x in range(0, n):
            line = []
            if i + 1 == p:
                for j in range(m * i, m * (i + 1) + 1):
                    if j > n:
                        line.append(0)
                    else:
                        line.append(mat1[x][j])
            else:
                for j in range(m * i, m * (i + 1)):
                    line.append(mat1[x][j])

            mat.append(line)
        lst.append(mat)
    return lst


def divideB(mat1, n):
    lst = []
    m = int(math.log2(n))
    p = int(n / m)
    for i in range(0, p):
        mat = []
        if i + 1 == p:
            for j in range(m * i, m * (i + 1) + 1):
                line = []
                for x in range(0, n):
                    if j > n:
                        line.append(0)
                    else:
                        line.append(mat1[j][x])
                mat.append(line)
        else:
            for x in range(m * i, m * (i + 1)):
                line = []
                for j in range(0, n):
                    line.append(mat1[x][j])
                mat.append(line)
        lst.append(mat)
    return lst


def sumB(mat1, mat2, n):
    matrix_to_ret = []
    for i in range(0, mat2.__len__()):
        lst_to_sum = []
        for j in range(0, mat2[0].__len__()):
            if mat2[i][j] != 0:
                lst_to_sum.append(mat1[j])
        result = []
        for y in range(0, n):
            x = 0
            for w in range(0, lst_to_sum.__len__()):
                if lst_to_sum[w][y] == 0 and x == 0:
                    x = 0
                else:
                    x = 1
            result.append(x)
        matrix_to_ret.append(result)

    return matrix_to_ret


# mat = [
#     [1, 1, 0, 0, 0],
#     [0, 0, 1, 1, 1],
#     [1, 0, 0, 1, 0],
#     [1, 0, 0, 1, 1],
#     [1, 0, 1, 0, 1]]
# mat2 = [
#     [0, 1, 0, 0, 1],
#     [0, 0, 0, 0, 0],
#     [1, 1, 0, 0, 1],
#     [1, 0, 1, 0, 0],
#     [1, 1, 0, 1, 0]]


def problema3(mat1, mat2, n):
    lst1 = divideA(mat1, n)
    lst2 = divideB(mat2, n)
    p = int(math.log2(n))
    mataux = []
    for i in range(0, p):
        mataux.append(sumB(lst2[i], lst1[i], n))
    final = []
    for i in range(0, n):
        x = []
        for j in range(0, n):
            x.append(0)
        final.append(x)
    for i in range(0, p):
        for j in range(0, n):
            for w in range(0, n):
                if mataux[i][j][w] == 0 and final[j][w] == 0:
                    final[j][w] = 0
                else:
                    final[j][w] = 1
    return final


# print(problema3(mat, mat, 5))
