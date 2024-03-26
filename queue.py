# rita huan zhou
# 2024-spring-cs-415 Midterm
# 0314/2024

def enqueue(x_list, item):
    x_list.append(item)


def dequeue(y_list):
    if len(y_list) == 0:
        return None
    else:
        first_item = y_list[0]
        y_list = y_list[1:]
        print(y_list)
        return first_item


