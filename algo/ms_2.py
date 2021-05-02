def sort(arr):
    if len(arr) <= 1:
        return
    mid = len(arr) // 2
    left_side = arr[:mid]
    right_side = arr[mid:]

    sort(left_side)
    sort(right_side)

    i = j = k = 0

    while i < len(left_side) and j < len(right_side):
        if left_side[i] <= right_side[j]:
            arr[k] = left_side[i]
            i += 1
            k += 1
        else:
            arr[k] = right_side[j]
            j += 1
            k += 1

    while i < len(left_side):
        arr[k] = left_side[i]
        k += 1
        i += 1

    while j < len(right_side):
        arr[k] = right_side[j]
        k += 1
        j += 1


arr = [324, -231, 21, 43, 0, 346, 69, 11, 33]
sort(arr)
print(arr)