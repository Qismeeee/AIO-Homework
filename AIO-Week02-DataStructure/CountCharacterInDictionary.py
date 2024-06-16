def count_characters(word):
    count_dict = {}
    for char in word:
        if char.isalpha():
            if char in count_dict:
                count_dict[char] += 1
            else:
                count_dict[char] = 1
    return count_dict


def main():
    word = input("Enter a word: ")
    result = count_characters(word)

    result_str = ""
    for char, count in result.items():
        result_str += f"'{char}': {count}, "
    result_str = result_str.rstrip(", ")

    print(result_str)


if __name__ == "__main__":
    main()
