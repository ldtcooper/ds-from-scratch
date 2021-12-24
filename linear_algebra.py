from typing import List, Tuple, Callable
import math

Vector = List[float]
Matrix = List[Vector]

def add(v1: Vector, v2: Vector) -> Vector:
    if len(v1) != len(v2):
        raise ValueError("Vectors are of differing lengths")
    return [v1[i] + v2[i] for i in range(len(v1))]


def subtract(v1: Vector, v2: Vector) -> Vector:
    if len(v1) != len(v2):
        raise ValueError("Vectors are of differing lengths")
    return [v1[i] - v2[i] for i in range(len(v1))]

def multiply(scalar: float, vector: Vector) -> Vector:
    return [scalar * el for el in vector]

def componentwise_sum(vectors: List[Vector]) -> Vector:
    first_len = len(vectors[0])
    if any(len(v) != first_len for v in vectors):
        raise ValueError("Vectors are of differing lengths")
    result = [0] * first_len
    for v in vectors:
        result = add(result, v)
    return result

def vector_mean(vectors: List[Vector]) -> Vector:
    first_len = len(vectors[0])
    n = len(vectors)
    if any(len(v) != first_len for v in vectors):
        raise ValueError("Vectors are of differing lengths")
    return multiply(1/n, componentwise_sum(vectors))

def dot_product(v1: Vector, v2: Vector) -> float:
    if len(v1) != len(v2):
        raise ValueError("Vectors are of differing lengths")
    products = [v1[i] * v2[i] for i in range(len(v1))]
    return sum(products)

def sum_of_squares(v: Vector) -> float:
    return dot_product(v, v)

def magnitude(v: Vector) -> float:
    return math.sqrt(sum_of_squares(v))

def squared_distance(v1: Vector, v2: Vector) -> float:
    return sum_of_squares(subtract(v1, v2))

def distance(v1: Vector, v2: Vector) -> float:
    return math.sqrt(squared_distance(v1, v2))

def shape(M: Matrix) -> Tuple[float, float]:
    rows = len(M)
    cols = len(M[0]) if M else 0
    return (rows, cols)

def get_row(M: Matrix, i: int) -> Vector:
    return M[i]

def get_col(M: Matrix, i: int) -> Vector:
    return [vec[i] for vec in M]

def make_matrix(rows: int, cols: int, make_fn: Callable[[int, int], float]) -> Matrix:
    return [[make_fn(i,j) for j in range(rows)] for i in range(cols)]

def identity_matrix(n: int) -> Matrix:
    return make_matrix(n, n, lambda a, b: 1 if a == b else 0)

def print_matrix(M: Matrix) -> None:
    for row in M:
        print(row)
    
assert componentwise_sum([[1, 2], [3, 4], [5, 6], [7, 8]]) == [16, 20]
assert vector_mean([[1, 2], [3, 4], [5, 6]]) == [3, 4]
assert dot_product([1, 2, 3], [4, 5, 6]) == 32
assert sum_of_squares([1, 2, 3]) == 14  # 1 * 1 + 2 * 2 + 3 * 3
assert magnitude([3, 4]) == 5
assert identity_matrix(5) == [[1, 0, 0, 0, 0],
                              [0, 1, 0, 0, 0],
                              [0, 0, 1, 0, 0],
                              [0, 0, 0, 1, 0],
                              [0, 0, 0, 0, 1]]

