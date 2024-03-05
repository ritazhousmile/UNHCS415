# Huan Zhou
# 04_Bubble_Sort
# 04/03/3024
import random
from punch_timer import punch_in, punch_out, punch_diff


def bubble_sort(unsorted_list):
    n = len(unsorted_list)

    for q in range(n):

        for j in range(0, n - q - 1):

            if unsorted_list[j] > unsorted_list[j + 1]:
                unsorted_list[j], unsorted_list[j + 1] = unsorted_list[j + 1], unsorted_list[j]


arr = []
arr_length = int(input("Enter the size of the list to sort: "))
if arr_length < 20:
    for i in range(arr_length):
        arr.append(random.randint(-100, 100))
    print(f"Unsorted List: {arr}")
    start_time = punch_in()
    bubble_sort(arr)
    end_time = punch_out()
    print(f"Sorted New List: {arr}")
    time_diff = punch_diff(start_time, end_time)
    print(f"This took {time_diff} nanoseconds")
