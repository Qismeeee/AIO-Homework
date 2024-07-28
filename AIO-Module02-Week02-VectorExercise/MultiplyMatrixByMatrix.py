import numpy as np

def matrix_multi_matrix(matrix1, matrix2):
    result = np.dot(matrix1, matrix2)

    return result

# m1 = np.array([[0, 1, 2], [2, -3, 1]])
# m2 = np.array([[1, -3], [6, 1], [0, -1]])
# result = matrix_multi_matrix(m1, m2)
# print(result)

m3 = np. array ([[1 , 2] , [3 , 4]])
m3 = np. reshape (m3 ,( -1 ,4), "F") [0]
m4 = np. array ([[1 , 1 , 1 , 1] ,[2 , 2 , 2 , 2] , [3 , 3 , 3 , 3] , [4 , 4 , 4 , 4]])
result = m3@m4
print(result)