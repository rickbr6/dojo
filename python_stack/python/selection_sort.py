def selection_sort(arr):

    current_idx = 0

    # Loop through one time for each element in the array
    while current_idx < len(arr)-1:

        # Set the pointer index for the current pass
        lowest_num_index = current_idx
        lowest_num = arr[lowest_num_index]

        # Check each remaining element to find the lowest value
        for i in range(current_idx + 1, len(arr)):
            if arr[i] < lowest_num:
                lowest_num = arr[i]
                lowest_num_index = i

        # swap the lowest value with the current index
        arr[current_idx], arr[lowest_num_index] = arr[lowest_num_index], arr[current_idx]

        # Increment for pointer for the next pass
        current_idx += 1

    return arr


print(selection_sort([50, 32, 2, 77, 25]))