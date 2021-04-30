def fib(n, memo = {}):
    if memo.get(n) != None:
        return memo[n]
    if n <= 2:
        return 1
    memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
    print(n, memo)
    return memo[n]

def fib2(n):
    if n <= 2:
        return 1
    calc = fib(n - 1) + fib(n - 2)
    return calc

print(fib(50))