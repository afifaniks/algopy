def minimumSwaps(arr):
    swaps = 0

    i = 0
    
    for i in range(len(arr)):
        if arr[i] == i + 1:
            continue

        j = i + 1

        while arr[j] != i + 1:
            j += 1

        arr[j], arr[i] = arr[i], arr[j]
        swaps += 1

    return swaps

print(minimumSwaps([1,3,5,2,4,6,7]))