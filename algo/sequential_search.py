def search(arr, key):
    for pos in range(0, len(arr)):
        if arr[pos] == key:
            return True
    return False

arr = [1, 435, 43, 22, 11, 67]

print(search(arr, 22))
print(search(arr, 69))