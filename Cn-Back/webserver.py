import scipy.linalg as la

from flask import Flask, request, jsonify
from flask_cors import CORS
from http import HTTPStatus


app = Flask(__name__)
CORS(app)


@app.route("/Tema1/p1", methods=["GET"])
def hw1_p1():
    import Tema1
    return jsonify(Tema1.problema1()), HTTPStatus.CREATED


@app.route("/Tema1/p2", methods=["GET"])
def hw1_p2():
    import Tema1
    return jsonify(Tema1.problema2()), HTTPStatus.CREATED


@app.route("/Tema1/p3", methods=["POST"])
def hw1_p3():
    mat1 = request.json.get("mat1")
    mat2 = request.json.get("mat2")

    if len(mat1) == len(mat2):
        import Tema1
        return jsonify(Tema1.problema3(mat1, mat2, len(mat1))), HTTPStatus.CREATED


@app.route("/Tema2/solve", methods=["POST"])
def hw2_solve():
    A_init = request.json.get("A_init")
    b_init = request.json.get("b_init")

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
            "result1": "{}{}{}".format(
                "||A_init * x - b_init||",
                result1,
                "[OK]" if result1 < eps else "[Not OK]"),
        }), HTTPStatus.CREATED


@app.route("/Tema2/inverted", methods=["POST"])
def hw2_inverted():
    A_init = request.json.get("A_init")
    b_init = request.json.get("b_init")

    if len(A_init) == len(b_init):
        import Tema2
        return jsonify(Tema2.inverse(A_init)), HTTPStatus.CREATED


@app.route("/Tema3/add", methods=["POST"])
def hw3_add():
    import Tema3
    a, _ = Tema3.load_matrix_from_string(request.json.get("a"))
    b, _ = Tema3.load_matrix_from_string(request.json.get("b"))
    if len(a) == len(b):
        return jsonify(Tema3.matrix_addition(a, b)), HTTPStatus.CREATED


@app.route("/Tema3/mult", methods=["POST"])
def hw3_mult():
    import Tema3
    Tema3.matrix_dot()


@app.route("/Tema4/solve", methods=["POST"])
def hw4_solve():
    import Tema4
    if Tema4.check_diagonal():
        Tema4.solve()


@app.route("/Tema6/solve/5squares", methods=["POST"])
def hw6_solve_5squares():
    import Tema6
    Tema6.five_squares()


@app.route("/Tema6/solve/interpolation", methods=["POST"])
def hw6_solve_interpolation():
    import Tema6
    Tema6.interpolation()


if __name__ == '__main__':
    print("Starting web server...")
    app.run(host="0.0.0.0", port=5000)
