import math

def is_number(x):
    try:
        float(x)
        return True
    except ValueError:
        return False
    return True

def sigmoid(x):
    return 1 / (1 + math.exp(-x))

def relu(x):
    return max(0, x)

def elu(x):
    if x > 0:
        return x
    else:
        return 0.01  * (math.exp(x) - 1)
    
def exercise2():
    x = input("Input x: ")
    if not is_number(x):
        print("x must be a number")
        return
    
    x = float(x)
    activation_function = input("Input activation function (sigmoid | relu | elu): ")
    
    if(activation_function == "sigmoid"):
        result = sigmoid(x)
        print(f'sigmoid: f({x}) = {result}')
    elif (activation_function == "relu"):
        result = relu(x)
        print(f'relu: f({x}) = {result}')
    elif (activation_function == "elu"):
        result = elu(x)
        print(f'elu: f({x}) = {result}')
    else:
        print(f'{activation_function} is not supported')


if __name__ == "__main__":
    exercise2()    