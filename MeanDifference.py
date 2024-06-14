def md_nre_single_sample(y, y_hat, n, p):
    root_y = y ** (1/n)
    root_y_hat = y_hat ** (1/n)
    error = (root_y - root_y_hat) ** p
    return error

def exercise5():
    try:
        y = float(input("Enter the value of y: "))
        y_hat = float(input("Enter the value of y_hat: "))
        n = int(input("Enter the value of n (positive integer): "))
        p = int(input("Enter the value of p (positive integer): "))

        if n <= 0 or p <= 0:
            raise ValueError("n and p must be positive integers")
    except ValueError as e:
        print(f"Invalid input: {e}")
        return

    result = md_nre_single_sample(y, y_hat, n, p)
    print(f"md_nre_single_sample(y={y}, y_hat={y_hat}, n={n}, p={p}) = {result}")

if __name__ == "__main__":
    exercise5()