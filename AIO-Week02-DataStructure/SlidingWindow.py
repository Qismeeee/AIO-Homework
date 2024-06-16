def max_sliding_window(num_list, k):
    if k < 1 or len(num_list) == 0 or k > len(num_list):
        return []
    result = []
    for i in range(len(num_list) - k + 1):
        window = num_list[i:i+k]
        max_value = max(window)
        result.append(max_value)
    return result


def input_data():
    while True:
        try:
            num_list = input("Enter a list of numbers: ")
            num_list = num_list.split()
            for i in range(len(num_list)):
                num_list[i] = int(num_list[i])
            # C2: num_list = list(map(int, input("Enter a list of numbers: ").split()))
            k = int(input("Enter the window size: "))
            if k >= 1:
                return num_list, k
            else:
                print(
                    "The value of k must be greater than or equal to 1. Please re-enter.")
        except ValueError:
            print("Invalid input. Please try again.")


def main():
    num_list, k = input_data()
    result = max_sliding_window(num_list, k)
    print(result)


if __name__ == "__main__":
    main()
