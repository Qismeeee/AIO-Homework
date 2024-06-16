def word_count(file_path):
    count_dict = {}
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            words = line.split()
            for word in words:
                if word in count_dict:
                    count_dict[word] += 1
                else:
                    count_dict[word] = 1
    return count_dict


file_path = 'E:/AIO_Homework/AIO-Exercises-Week02-DataStructure/P1_data.txt'
result = word_count(file_path)
print(result)
