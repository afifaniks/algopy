def repeatedString(s, n):
    # Write your code here
    length = len(s)
    multiples = n//length

    remainder = n - (length*multiples)

    a_ctr = 0

    for ch in s:
        if ch == 'a':
            a_ctr += 1

    a_ctr = multiples * a_ctr

    for ch in s[:remainder]:
        if ch == 'a':
            a_ctr += 1

    return a_ctr


print(repeatedString('aba', 10))