# huan zhou
# 2024 spring -cs 415 midterm
# 3 0314/2024

"""
def split_list(split_count, values):
    list = []
    for i in range(split_count):
        list1 = []
        if len(values) % split_count != 0:
            for j in range(len(values)//split_count+1):
                if i+j*split_count >= len(values):
                    break
                else:
                    list1.append(values[i+j*split_count])
        else:
            for j in range((len(values)//split_count)):
                list1.append(values[i + j*split_count])
        list.append(list1)
    print(list)

split_list(6, [1,2,3,4,5,6,7,8,9,10,11])
"""


def split_list(split_count, values):
    a_list = []
    for i in range(split_count):
        a_list.append([])
    for i in range(len(values)):
        print(i % split_count)
        a_list[i % split_count].append(values[i])
    print(a_list)


split_list(5, [1, 2, 3, 4, 5, 6, 7, 8, 9])
