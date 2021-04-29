def arrayManipulation(n, queries):
    arr = [0] * n

    max = -1

    for i in range(n):
            for query in queries:
                start = query[0] - 1
                stop = query[1]

                if i >= start and i < stop:
                    arr[i] += query[2]
                    if arr[i] > max:
                        max = arr[i]

    return max


print(arrayManipulation(10, [[1, 5, 3], [4, 8, 7], [6, 9, 1]]))