import timeit

dot_product_1000_to_1000="""

l1 = np.random.random_integers(0, 1, (1000, ))
connections = np.random.random_integers(0,1, (1000, 1000))
l2 = np.dot(connections, l1)

"""

dot_product_5000_to_5000="""

l1 = np.random.random_integers(0, 1, (5000, ))
connections = np.random.random_integers(0,1, (5000, 5000))
l2 = np.dot(connections, l1)

"""

dot_product_10000_to_10000="""

l1 = np.random.random_integers(0, 1, (10000, ))
connections = np.random.random_integers(0,1, (10000, 10000))
l2 = np.dot(connections, l1)

"""

dot_product_50000_to_50000="""

l1 = np.random.randint(0, 1, (100000, ),dtype='int8')
connections = np.random.randint(0,1, (100000, 100000), dtype='int8')
l2 = np.dot(connections, l1)

"""

print(timeit.timeit(dot_product_1000_to_1000, number=3, setup="import numpy as np"))
print(timeit.timeit(dot_product_5000_to_5000, number=3, setup="import numpy as np"))
print(timeit.timeit(dot_product_10000_to_10000, number=3, setup="import numpy as np"))
print(timeit.timeit(dot_product_50000_to_50000, number=1, setup="import numpy as np"))