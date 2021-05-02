def partition(arr, lo, hi):
    i = lo
    pivot = arr[hi]

    for j in range(lo, hi):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    arr[hi], arr[i] = arr[i], arr[hi]

    return i


def quicky(arr, lo, hi):
    if lo >= hi:
        return
    pi = partition(arr, lo, hi)
    quicky(arr, lo, pi - 1)
    quicky(arr, pi + 1, hi)


def maximumToys(prices, k):
    quicky(prices, 0, len(prices) - 1)

    tot = 0
    ctr = 0

    for price in prices:
        if (tot + price) <= k:
            ctr += 1
            tot += price

    return ctr


print(maximumToys([1, 12, 5, 111, 200, 1000, 10], 50))
