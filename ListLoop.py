# Huan ZHou
# 08-List Loop Lab
# 02/20/2024
import statistics


def list_stats(int_list):
    maximum_value = int_list[0]
    minimum_value = int_list[0]
    su_value = 0
    if len(int_list) == 0:
        return None, None, None
    for x in int_list:
        if x > maximum_value:
            maximum_value = x
        elif x < minimum_value:
            minimum_value = x
        else:
            su_value += x
    av_value = su_value / len(int_list)
    return maximum_value, minimum_value, av_value


def check_work(numbers):
    min_value = min(numbers)
    max_value = max(numbers)
    a_value = statistics.mean(numbers)
    return min_value, max_value, a_value


number_list = []
for x in range(0, 50):
    number_list.append(x)
print(number_list)
maximum_value, minimum_value, ave_value = list_stats(number_list)
print(f"Maximum Value in array: {maximum_value}")
print(f"Minimum Value in array: {minimum_value}")
print(f"Average Value in array: {ave_value}")
if maximum_value is None or minimum_value is None or ave_value is None:
    print("Error: Empty list Provided.")
else:
    minValue, maxValue, aveValue = check_work(number_list)
    print(f"Maximum Value in array: {maxValue}")
    print(f"Minimum Value in array: {minValue}")
    print(f"Average Value in array: {aveValue}")
    if maximum_value == maxValue and minimum_value == minValue and ave_value == aveValue:
        print("All Statistics match")
