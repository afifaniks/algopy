def partition(arr, lo, hi):
    i = lo
    pivot = arr[hi]

    for j in range(lo, hi):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[hi] = arr[hi], arr[i]

    return i


def sort(arr, lo, hi):
    if lo >= hi:
        return

    pi = partition(arr, lo, hi)

    sort(arr, lo, pi - 1)
    sort(arr, pi + 1, hi)

arr = [23, 11, -88, 0, 1123, 32]
sort(arr, 0, 5)
print(arr)
