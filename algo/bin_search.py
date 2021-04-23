def search(arr, key):
    if len(arr) == 0:
        return False

    mid = len(arr) // 2

    if arr[mid] == key:
        return True
    elif arr[mid] < key:
        return search(arr[mid+1:], key)
    else:
        return search(arr[:mid], key)


arr = [1, 55, 66, 77, 223, 4343]
print(search(arr, 223))