def sort(arr):
    for i in range(len(arr)):
        max_pos = 0
        for j in range(len(arr) - i):
            if arr[j] > arr[max_pos]:
                max_pos = j
        arr[len(arr) - i], arr[max_pos] = arr[max_pos], arr[len(arr) - i]

    return arr


my_arr = [22, -1, 12, 234, 34, 2345, -72, 0]
my_arr = sort(my_arr)
print(my_arr)