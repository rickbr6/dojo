def insertion_sort(arr):
    # Basically, this sort works by starting at index 1, shifting that value to the left until it is sorted
    # relative to all values to the left, and then moving on to the next index position and performing the same
    # shifts until the end of the list is reached.

    max_passes = len(arr)-1
    print('Max passes will be:', max_passes)

    for current_index in range(1, max_passes):
        print('Current Array for pass:', current_index, arr)

        # Check the value ant the current index and copy to temp if greater than the previous index value
        if arr[current_index] < arr[current_index-1]:
            temp_val = arr[current_index]

            # check the previous index values and move them up if greater than temp
            for i in range(current_index, 0, -1):
                if i <

                if arr[i-1] > temp_val:
                    arr[i] = arr[i-1]
                # When temp is greater than the current value drop it into that index
                else:
                    arr[i-1] = temp_val













print(insertion_sort([6, 5, 3, 1, 8, 7, 2, 4]))







