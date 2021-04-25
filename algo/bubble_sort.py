def sort(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

my_arr = [22, -1, 12, 234, 34, 2345, -3272, 0]
my_arr = sort(my_arr)
print(my_arr)