import numpy as np

# vector là 1 mảng numpy
def compute_vector_length(vector):
    norm = np.sqrt(np.sum([v**2 for v in vector]))

    return norm

vector = np.array([-2, 4, 9, 21])
result = compute_vector_length([vector]) # truyền vào 1 ds chứa 1 mảng numpy
print(round(result, 2))