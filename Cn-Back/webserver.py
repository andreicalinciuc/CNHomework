import numpy as np
import scipy.linalg as la

from flask import Flask, request, jsonify
from flask_cors import CORS
from http import HTTPStatus


app = Flask(__name__)
CORS(app)


eps = np.float_power(10, -10)


@app.route("/Tema1/p1", methods=["GET"])
def hw1_p1():
    import Tema1
    return jsonify({"result": Tema1.problema1()}), HTTPStatus.CREATED


@app.route("/Tema1/p2", methods=["GET"])
def hw1_p2():
    import Tema1
    return jsonify({"result": Tema1.problema2(real=False)}), HTTPStatus.CREATED


@app.route("/Tema1/p3", methods=["POST"])
def hw1_p3():
    mat1 = request.json.get("mat1")
    mat2 = request.json.get("mat2")

    mat1 = [[int(cell) for cell in row.split(",")] for row in mat1.split("\n")]
    mat2 = [[int(cell) for cell in row.split(",")] for row in mat2.split("\n")]

    import Tema1
    return jsonify(Tema1.problema3(mat1, mat2, len(mat1))), HTTPStatus.CREATED


def get_result(string, value, eps):
    return "{}: {} [{}]".format(string, value, "OK" if value < eps else "Not OK")


# Tema 2
# ---------------
# A_init:
# 2.5, 2, 2
# 5, 6, 5
# 5, 6, 6.5
# ---------------
# b_init
# 2, 2, 2
@app.route("/Tema2", methods=["POST"])
def hw2_solve():
    A_init = request.json.get("A_init")
    b_init = request.json.get("b_init")

    A_init = [[float(cell) for cell in row.split(",")] for row in A_init.split("\n")]
    b_init = [float(cell) for cell in b_init.split(",")]

    if len(A_init) == len(b_init):
        import Tema2
        x_LU, result1 = Tema2.manual_compute_solution(A_init, b_init, display=False)
        x_lib = la.lu_solve(la.lu_factor(A_init), b_init, trans=0)
        result2 = la.norm(x_LU - x_lib)
        A_init_lib_inv = la.inv(A_init)
        result3 = la.norm(x_LU - A_init_lib_inv.dot(b_init))
        A_LU_inv = Tema2.inverse(A_init)
        result4 = la.norm(A_LU_inv - A_init_lib_inv)
        return jsonify({
            "result1": get_result("||A_init * x - b_init||", result1, eps),
            "result2": get_result("||x_LU - x_lib||", result2, eps),
            "result3": get_result("||x_LU - A_lib_inv * b_init||", result3, eps),
            "result4": get_result("||A_LU_inv - A_lib_inv||", result4, eps)
        }), HTTPStatus.CREATED


# Tema 3
# Sunt cele 4 fisiere din Tema3_input
@app.route("/Tema3", methods=["POST"])
def hw3_add():
    import Tema3
    a, n = Tema3.load_matrix_from_string(request.json.get("a"))
    b, _ = Tema3.load_matrix_from_string(request.json.get("b"))
    aplusb, _ = Tema3.load_matrix_from_string(request.json.get("aplusb"))
    aorib, _ = Tema3.load_matrix_from_string(request.json.get("aorib"))
    a_plus_b_calculated = Tema3.matrix_addition(a, b)
    a_ori_b_calculated = Tema3.matrix_dot(a, b, n)
    return jsonify({
        "a_plus_b": get_result(
            "A + B",
            0 if Tema3.check_equal_matrix(aplusb, a_plus_b_calculated, n) else 1,
            eps
        ),
        "a_ori_b": get_result(
            "A * B",
            0 if Tema3.check_equal_matrix(aorib, a_ori_b_calculated, n) else 1,
            eps
        )
    }), HTTPStatus.CREATED


# Tema 4
# 2 inputs, sunt cele din folderul Tema4_input (a_i.txt, b_i.txt)
@app.route("/Tema4/solve", methods=["POST"])
def hw4_solve():
    import Tema4
    a, n = Tema4.load_matrix_from_string(request.json.get("a"))
    b, _ = Tema4.load_vector_from_string(request.json.get("b"))
    if Tema4.check_diagonal(a, n):
        x = Tema4.solve(a, b, n)
        return jsonify({
            "result": get_result(
                "||A * X - b||",
                0 if Tema4.check_solution(a, b, x) else 1,
                eps
            )
        }), HTTPStatus.CREATED


#   {
#        "test_index": 0,
#        "x_0": -1,
#        "x_n": 2
#   }
@app.route("/Tema6/solve/5squares", methods=["POST"])
def hw6_solve_5squares():
    import Tema6
    test_index = request.json.get("test_index")
    test_params = list(Tema6.tests.values())[test_index]
    test_params[0] = request.json.get("x_0", test_params[0])
    test_params[1] = request.json.get("x_n", test_params[1])
    return jsonify(Tema6.five_squares(*test_params)), HTTPStatus.CREATED


#   {
#        "test_index": 0,
#        "x_0": -1,
#        "x_n": 2
#   }
@app.route("/Tema6/solve/interpolation", methods=["POST"])
def hw6_solve_interpolation():
    import Tema6
    test_index = request.json.get("test_index")
    test_params = list(Tema6.tests.values())[test_index]
    test_params[0] = request.json.get("x_0", test_params[0])
    test_params[1] = request.json.get("x_n", test_params[1])
    return jsonify(Tema6.five_squares(*test_params)), HTTPStatus.CREATED


#   {
#        "test_index": 0
#   }
@app.route("/Tema7/solve", methods=["POST"])
def hw7_solve():
    import Tema7
    test_index = request.json.get("test_index")
    test_params = list(Tema7.tests.values())[test_index]
    return jsonify(Tema7.solve(*test_params)), HTTPStatus.CREATED


if __name__ == '__main__':
    print("Starting web server...")
    app.run(host="0.0.0.0", port=5000)
