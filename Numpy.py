import numpy as np

a = 0
b = 100
c = 3

matrix1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix2 = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])

numbers = np.array([1, 2, 3, 4, 5])
matrix = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]]) 
zeros = np.zeros(5)
ones = np.ones((5, 5))
matrix_zeros = np.zeros_like(matrix)
matrix_ones = np.zeros_like(ones)
array_range = np.arange(a, b + 1, 5)
array_linspace = np.linspace(a, b, c) # a: From, b: To, c: How mutch, pas = (b - 1) / (c - 1) # Output: [0.  50. 100.]
array_random = np.random.rand(4)
matrix_random_int = np.random.randint(0, 10, (4, 4))
matrix_dot = matrix1.dot(matrix2) # dot(): La multiplication matricielle
matrix_concat1 = np.concatenate((matrix1, matrix2), axis = 0) 
# Output:
# [[ 1  2  3]
#  [ 4  5  6]
#  [ 7  8  9]
#  [10 20 30]
#  [40 50 60]
#  [70 80 90]]
matrix_concat2 = np.concatenate((matrix1, matrix2), axis = 1) 
# Output:
# [[ 1  2  3 10 20 30]
#  [ 4  5  6 40 50 60]
#  [ 7  8  9 70 80 90]]
number_dimention = numbers.ndim # The number of dimensions 1
number_shape = numbers.shape

print(number_shape)