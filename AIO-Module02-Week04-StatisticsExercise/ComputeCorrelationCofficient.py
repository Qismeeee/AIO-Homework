import numpy as np

def compute_correlation_cofficient(X, Y):
    N = len(X)
    numerator = 0
    denominator = 0

    sum_x = np.sum(X)
    sum_y = np.sum(Y)
    sum_xy = np.sum(X * Y)
    sum_x_squared = np.sum(X**2)
    sum_y_squared = np.sum(Y**2)

    numerator = N *  sum_xy - sum_x * sum_y
    denominator = np.sqrt((N * sum_x_squared - sum_x**2) * (N * sum_y_squared - sum_y**2))

    return np.round(numerator / denominator, 2)

X = np.asarray([-2, -5, -11, 6, 4, 15, 9])
Y = np.asarray([4, 25, 121, 36, 16, 225, 81])
print("Correlation: ", compute_correlation_cofficient(X, Y))