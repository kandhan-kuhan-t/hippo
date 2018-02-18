import numpy as np
import timeit


def a(
        vector: np.ndarray,
        matrix: np.ndarray
):
    resp = []
    for i in range(0, len(vector)):
        resp.append(np.multiply(vector[i], matrix[i]))
    return resp


def b(
        vector: np.ndarray,
        matrix: np.ndarray
):
    return np.multiply(
        vector,
        matrix
    )


test_a = timeit.timeit("""a(vector, matrix)""",
                       number=10, setup="""from __main__ import a;import numpy as n;vector=n.full((10000, ), dtype='float', fill_value=1);matrix=n.full((10000,9000), dtype='float', fill_value=0.2);"""
                       )
test_b = timeit.timeit("""b(vector, matrix.T)""",
                       number=10, setup="""from __main__ import b;import numpy as n;vector=n.full((10000, ), dtype='float', fill_value=1);matrix=n.full((10000,9000), dtype='float', fill_value=0.2);"""
                       )