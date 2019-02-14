def biggie_size(new_list):
    for i, val in enumerate(new_list):
        if val > 0:
            new_list[i] = "big"
    return new_list

# print(biggie_size([-1, 3, 5, -5]))


def count_positives(new_list):
    count = 0
    for val in new_list:
        if val > 0:
            count += 1
    new_list[-1] = count
    return new_list


# print(count_positives([1, 6, -4, -2, -7, -2]))


def sum_total(new_list):

    list_sum = 0
    for i, val in enumerate(new_list):
        list_sum += new_list[i]
    return list_sum


# print(sum_total([1, 2, 3, 4]))


def average(new_list):
    list_sum = 0
    for i, val in enumerate(new_list):
        list_sum += new_list[i]
    return list_sum / len(new_list)

# print(average([1, 2, 3, 4]))


def length(new_list):
    return len(new_list)


# print(length([]))


def ult(new_list):

    ult_dict = {}
    sum_total = 0
    min_val = new_list[0]
    max_val = new_list[0]
    for i, val in enumerate(new_list):
        sum_total += new_list[i]
        if new_list[i] < min_val:
            min_val = new_list[i]
        elif new_list[i] > max_val:
            max_val = new_list[i]

    length = len(new_list)
    average = sum_total / length

    ult_dict['sumTotal'] = sum_total
    ult_dict['average'] = average
    ult_dict['minimum'] = min_val
    ult_dict['maximum'] = max_val

    return ult_dict


print(ult([37, 2, 1, -9]))



