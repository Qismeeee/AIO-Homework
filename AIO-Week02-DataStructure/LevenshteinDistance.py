def levenshtein_distance(s, t):
    # Tạo bảng khoảng cách
    m, n = len(s), len(t)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Khởi tạo giá trị cho hàng đầu tiên và cột đầu tiên
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    # Tính toán khoảng cách Levenshtein
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s[i - 1] == t[j - 1]:
                cost = 0
            else:
                cost = 1
            dp[i][j] = min(dp[i - 1][j] + 1,      # Xóa
                           dp[i][j - 1] + 1,      # Thêm
                           dp[i - 1][j - 1] + cost)  # Thay thế

    return dp[m][n]

# Hàm nhập liệu từ người dùng


def get_input():
    source = input("Enter the source string: ")
    target = input("Enter the target string: ")
    return source, target

# Chương trình chính


def main():
    source, target = get_input()
    distance = levenshtein_distance(source, target)
    print(
        f"The Levenshtein distance between '{source}' and '{target}' is {distance}")


if __name__ == "__main__":
    main()
