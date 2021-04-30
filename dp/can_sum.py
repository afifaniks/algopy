def can_sum(n, arr, memo = {}):
    if memo.get(n) != None:
        return memo[n]
    if n == 0:
        return True
    if n < 0:
        return False
    for i in arr:
        if can_sum(n - i, arr, memo):
            memo[n] = True
            return True

    memo[n] = False
    return False


print(can_sum(300, [7, 14]))
