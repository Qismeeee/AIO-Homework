import math
import random

# Kiểm tra nếu là chuỗi thì chuyển chuỗi thành số


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
    return True


def mae(targets, predictions):
    n = len(targets)
    return sum(abs(t - p) for t, p in zip(targets, predictions)) / n


def mse(targets, predictions):
    n = len(targets)
    return sum((t - p) ** 2 for t, p in zip(targets, predictions)) / n


def rmse(targets, predictions):
    return math.sqrt(mse(targets, predictions))


def exercise3():
    num_samples = input(
        "Input number of samples (integer number) which are generated: ")
    if not num_samples.isnumeric():
        print("Number of samples must be an integer number")
        return

    num_samples = int(num_samples)
    loss_name = input("Input loss name (MAE, MSE, RMSE): ").upper()

    targets = [random.uniform(0, 10) for _ in range(num_samples)]
    predictions = [random.uniform(0, 10) for _ in range(num_samples)]

    if loss_name == "MAE":
        loss = mae(targets, predictions)
    elif loss_name == "MSE":
        loss = mse(targets, predictions)
    elif loss_name == "RMSE":
        loss = rmse(targets, predictions)
    else:
        print(f'{loss_name} is not supported')
        return

    for i in range(num_samples):
        if loss_name == "MAE":
            sample_loss = abs(targets[i] - predictions[i])
        elif loss_name == "MSE" or loss_name == "RMSE":
            sample_loss = (targets[i] - predictions[i]) ** 2

        print(
            f'loss name: {loss_name}, sample: {i}, pred: {predictions[i]}, target: {targets[i]}, loss: {sample_loss}')

    print(f'final {loss_name}: {loss}')


if __name__ == "__main__":
    exercise3()
