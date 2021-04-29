def minimumBribes(q):
    bribes = 0
    chaotic = False
    for i in range(0, len(q)):
        if q[i] > (i + 1):
            bribe = (q[i] - (i + 1))
            bribes += bribe

            if bribe > 2:
                chaotic = True

    if chaotic:
        print("Too chaotic")
    else:
        print(bribes)

minimumBribes([1,2,5,3,7,8,6,4])
minimumBribes([5, 1, 2, 3, 7, 8, 6, 4])
minimumBribes([i for i in range(1, 10)])
minimumBribes([2,1,5,3,4])
