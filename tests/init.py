# this is just various tests to help understand ML

import matplotlib.pyplot as pyplot   # conda install -c conda-forge matplotlib
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_moons
import numpy as np

matrix = np.array([
    [1, 2, 3], [4, 5, 6], [7, 8, 9]
])

print(matrix)


allBool = np.ones([10, 4], dtype=np.bool)
print(allBool)

print("-"*50)
# Understanding weights


array1 = np.array([1, 2, 3])

weight1 = np.array([[1, 1, 1], [2, 2, 2, ], [3, 3, 3]])

calculate1 = np.dot(array1, weight1)

print("Using Array {} \nWith weights \n{} \nGets the answer: \n{}".format(
    array1, weight1, calculate1))


# Using dot is basiclly matrix multiplication

print("-"*50)

# Vectorization


def doAdd(a, b):
    return a + b


vectAdd = np.vectorize(doAdd)

print(vectAdd([1, 2, 3, 4], [2, 3, 4, 5]))


#
print("-"*50)
# Building basic nerual network:


def init(inp, out):
    return np.random.randn(inp, out)/np.sqrt(inp)


def create_architecture(input_layer, first_layer, output_layer, random_seed=0):
    np.random.seed(random_seed)
    layers = X.shape[1], 3, 1
    arch = list(zip(layers[:-1], layers[1:]))
    weights = [init(inp, out) for inp, out in arch]
    return weights


print(create_architecture(1, 2, 3, 0))
