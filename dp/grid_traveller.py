def grid_traveller(m, n, memo = {}):
    if m == 1 and n == 1:
        return 1
    if m < 1 or n < 1:
        return 0

    key = str(m) + "," + str(n)
    key2 = str(n) + "," + str(m)

    if memo.get(key) != None:
        return memo[key]

    if memo.get(key2) != None:
        return memo[key2]

    memo[key] = grid_traveller(m - 1, n, memo) + grid_traveller(m, n - 1, memo)

    return memo[key]

print(grid_traveller(18, 18))