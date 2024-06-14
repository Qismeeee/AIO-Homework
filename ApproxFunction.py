import math


def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


def approx_sin(x, n):
    result = 0
    for i in range(n):
        term = ((-1) ** i) * (x ** (2*i + 1)) / factorial(2*i + 1)
        result += term
    return result


def approx_cos(x, n):
    result = 0
    for i in range(n):
        term = ((-1) ** i) * (x ** (2*i)) / factorial(2*i)
        result += term
    return result


def approx_sinh(x, n):
    result = 0
    for i in range(n):
        term = (x ** (2 * i + 1)) / factorial(2 * i + 1)
        result += term
    return result


def approx_cosh(x, n):
    result = 0
    for i in range(n):
        term = (x ** (2 * i)) / factorial(2 * i)
        result += term
    return result


def exercise4():
    x = input("Enter the value of x (in radians): ")
    n = input("Enter the number of terms (positive integer): ")

    try:
        x = float(x)
        n = int(n)
        if n <= 0:
            raise ValueError("The number of terms must be a positive integer")
    except ValueError as e:
        print(f"Invalid input: {e}")
        return

    sin_result = approx_sin(x, n)
    cos_result = approx_cos(x, n)
    sinh_result = approx_sinh(x, n)
    cosh_result = approx_cosh(x, n)

    print(f"approx_sin(x={x}, n={n}) = {sin_result}")
    print(f"approx_cos(x={x}, n={n}) = {cos_result}")
    print(f"approx_sinh(x={x}, n={n}) = {sinh_result}")
    print(f"approx_cosh(x={x}, n={n}) = {cosh_result}")


if __name__ == "__main__":
    exercise4()
