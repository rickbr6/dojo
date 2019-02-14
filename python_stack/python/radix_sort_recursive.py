import timeit


def get_digit(num, place):
    """
    :param num: A single or multi digit number
    :param place: A number representing the place value of the number to return. i.e, 1 would represent the ones
        position and 2 would represent the 10s position.
    :return: Returns the number in the position requested with the place parameter. For the request with args (345,2)
        the return value would be 4 (since 2 represents the tens position).
    """

    if len(str(num)) < place:
        return 0
    else:
        number = (str(num))[-place]
        return int(number)


def get_max_iterations(num_array):
    """
    :param num_array: An array of numbers
    :return: Returns the length value of the longest number in the array. For example: [1, 10, 300, 4) would return 3
        which is the length of the longest value(300).
    """
    max_num = 0
    for num in num_array:
        if len(str(num)) > max_num:
            max_num = len(str(num))
    return max_num


def radix_sort(numbers, place=1, count=1):
    """
    :param numbers: The array of numbers to sort.
    :param place: Represents the current place value to use for sorting. 1 is the ones place, 2 is the tens place,
        3 is the hundreds place etc. Defaults to 1 and is only used by the recursive function call.
    :param count: Tracks the number of times the function has been called. Defaults to 1 and is only used by the
        recursive function call.
    :return: Returns the original array sorted by value.
    """

    # Determines how many times we need to iterate through the array based on the length of the largest number
    # in the array.
    max_iterations = get_max_iterations(numbers)

    # Sort each number into the appropriate bucket based on the current place number
    buckets = [[], [], [], [], [], [], [], [], [], []]
    for num in numbers:
        current_num = get_digit(num, place)
        buckets[current_num].append(num)

    # add the numbers back to the numbers array
    index = 0
    for bucket in buckets:
        for digit in bucket:
            numbers[index] = digit
            index += 1

    if count <= max_iterations:
        count += 1
        place += 1
        radix_sort(numbers, place, count)
    return numbers


# Test
sorted_array = radix_sort([3221, 1, 10, 23456, 9680, 577, 9420, 7, 5622, 4793, 2030, 3138, 82, 2599, 743, 4127, 894837])
print(sorted_array)
