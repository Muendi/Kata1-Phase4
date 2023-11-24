def find_unsorted_subarray(arr):
    n = len(arr)
    start = 0
    end = n - 1

    # Start index of the unsorted subarray
    while start < n - 1 and arr[start] <= arr[start + 1]:
        start += 1

    if start == n - 1:
        # Array is already sorted
        return [0, 0]

    #End index of the unsorted subarray
    while end > 0 and arr[end] >= arr[end - 1]:
        end -= 1

    #Minimum and maximum values within the unsorted subarray
    min_val = min(arr[start:end + 1])
    max_val = max(arr[start:end + 1])

    # Include elements that need to be sorted
    while start > 0 and arr[start - 1] > min_val:
        start -= 1

    while end < n - 1 and arr[end + 1] < max_val:
        end += 1

    return [start, end]

arr = [1, 2, 3, 6, 4, 4]
result = find_unsorted_subarray(arr)
print(result)
