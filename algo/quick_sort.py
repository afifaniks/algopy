def quick_sort(arr):
    length = len(arr)

    if length <= 1:
        return arr

    pivot = arr.pop()

    left_subseq = []
    right_subseq = []

    for i in arr:
        if i < pivot:
            left_subseq.append(i)
        else:
            right_subseq.append(i)

    return quick_sort(left_subseq) + [pivot] + quick_sort(right_subseq)


print(quick_sort([22, 45, 1, 2, 0, -33]))