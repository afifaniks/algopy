def hourglassSum(arr):
    row_start = 0
    col_start = 0

    max = None

    while row_start <= 3 and col_start <= 3:
        mat_sum = 0
        for i in range(row_start, row_start + 3):
            for j in range(col_start, col_start + 3):
                if (i == row_start + 1 and j == col_start or
                        i == row_start + 1 and j == col_start + 2):
                    continue
                mat_sum += arr[i][j]
        col_start += 1

        if max == None:
            max = mat_sum
        else:
            if mat_sum > max:
                max = mat_sum

        if col_start == 4:
            row_start += 1
            col_start = 0
    return max

arr = [
    [-9, -9, -9, 1, 1, 1],
    [0, -9,  0,  4, 3, 2],
    [-9, -9, -9,  1, 2, 3],
    [ 0,  0,  8 , 6, 6, 0],
    [ 0,  0 , 0, -2, 0, 0],
    [0,  0,  1,  2, 4, 0]
]

print(hourglassSum(arr))



