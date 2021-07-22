"""Given an integer square (n by n) matrix, return its transpose. A transpose of a matrix switches the row and column indices. That is, for every r and c, matrix[r][c] = matrix[c][r].

Constraints

    n ≤ 100

"""

def solve_for_loop(matrix):

    if len(matrix)==0:
        return []

    results = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    return results

def solve_zip(matrix):
    if len(matrix)==0:
        return []

    else:
        return list(zip(*matrix))

