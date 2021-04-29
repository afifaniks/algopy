def sockMerchant(n, ar):
    # Write your code here
    counter = {}

    for i in ar:
        if i in counter:
            current = counter[i]
            current += 1
            counter[i] = current
        else:
            counter[i] = 1

    pairs = 0
    for i in counter:
        if counter[i] % 2 == 0:
            pairs += (counter[i]//2)
        else:
            pairs += ((counter[i] - 1) // 2)

    return pairs

print(sockMerchant(9, [10, 20, 20, 10, 10, 30, 50, 10, 20]))