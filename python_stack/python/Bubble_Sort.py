def bubble_sort(arr):
    count = 1

    # Perform the swapping loop until there are 0 swaps done
    while not count == 0:

        # Keep track of the number of time a swap is performed
        count = 0

        # loop through the array and swap if necessary
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                count += 1
                arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr


# print(bubble_sort([1, 5, 4, 3, 6, 7, 5, 2, 10 , 20, 15, 14, 13, 12, 11]))
