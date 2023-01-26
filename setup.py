def BubbleSort(list):
    for i in range(len(list) - 1):
        for j in range(len(list) - 1 - i):
            if list[j] > list[j + 1]:
                tem = list[j]
                list[j] = list[j + 1]
                list[j + 1] = tem

    return list


list1 = [10, 5, 6, 3, 7]
print(BubbleSort(list1))
print("hahhhahaha")
print("test")
print(123124)