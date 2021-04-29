def nearlySimilarRectangles(sides):
    length = len(sides)
    count = 0

    for i in range(length):
        a = sides[i][0]
        b = sides[i][1]

        for j in range(i + 1, length):
            if i == j:
                continue

            c = sides[j][0]
            d = sides[j][1]

            if a*d == b*c:
                count += 1

    return count

