
def countdown(num):
    cd_list = []
    for i in range(num, -1, -1):
        cd_list.append(i)
    return cd_list


# print(countdown(5))

def print_return(x, y):
    print(x)
    return y


# print_return(1, 2)


def first_plus_len(new_list):
    return new_list[0] + len(new_list)


# print(first_plus_len([1, 2, 3, 4, 5]))


def val_greater_than_second(original_list):
    count = 0
    new_list = []
    for num in original_list:
        if num > original_list[1]:
            new_list.append(num)
            count += 1
    if count > 2:
        print(count)
        return new_list
    else:
        return False

print(val_greater_than_second([5,2]))


def this_len_that_val(size, value):
    new_list = []
    for i in range(0, size):
        new_list.append(value)
    return new_list


print(this_len_that_val(6, 2))









