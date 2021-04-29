def jumpingOnClouds(c):
    ctr = 0
    i = 0

    while i < len(c):
        if i < len(c) - 2:
            if c[i + 2] == 0:
                ctr += 1
                i += 2
            else:
                i += 1
                ctr += 1
        else:
            i += 1
            ctr += 1

    return ctr - 1


print(jumpingOnClouds([0,0,0,1,0,0]))
