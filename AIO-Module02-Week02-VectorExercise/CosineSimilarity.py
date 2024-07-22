import numpy as np
from numpy import dot
from numpy.linalg import norm

def compute_dot_product(vector1, vector2):
    result = np.dot(vector1, vector2)

    return result

def compute_vector_length(vector):
    norm = np.sqrt(np.sum([v**2 for v in vector]))

    return norm


def compute_cosine(v1, v2):
    cos_sim = compute_dot_product(v1, v2) / (compute_vector_length(v1) * compute_vector_length(v2))
    return cos_sim

x = np.array([1, 2, 3, 4])
y = np.array([1, 0, 3, 0])
result = compute_cosine(x, y)
print(result)