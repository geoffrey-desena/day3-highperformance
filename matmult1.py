# =============================================================================
# I asked chatGPT for help interpreting the results of the Spyder profiling
# tool. It rewrote matmult.py to be more modular. This makes the profiling
# much clearer. The whole script is spending 167 ms in multiply_matrices,
# which is the heaviest operation. However, calling randint also takes
# 133 ms for each call. So in the end, creating the matrices takes more
# time than calling them.
# =============================================================================

import random

N = 250

def create_square_matrix(n):
    matrix = []
    for i in range(n):
        matrix.append([random.randint(0, 100) for _ in range(n)])
    return matrix

def create_rectangular_matrix(n):
    matrix = []
    for i in range(n):
        matrix.append([random.randint(0, 100) for _ in range(n + 1)])
    return matrix

def create_result_matrix(n):
    result = []
    for i in range(n):
        result.append([0] * (n + 1))
    return result

def multiply_matrices(X, Y):
    rows_x = len(X)
    cols_y = len(Y[0])
    rows_y = len(Y)

    result = create_result_matrix(rows_x)

    for i in range(rows_x):
        for j in range(cols_y):
            for k in range(rows_y):
                result[i][j] += X[i][k] * Y[k][j]

    return result

def main():
    X = create_square_matrix(N)
    Y = create_rectangular_matrix(N)
    result = multiply_matrices(X, Y)

    for row in result:
        print(row)

if __name__ == "__main__":
    main()