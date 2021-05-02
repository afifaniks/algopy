import math


def encryption(s):
    no_sp = ""
    length = 0
    for c in s:
        if c != ' ':
            no_sp += c
            length += 1

    root = math.sqrt(length)

    col = math.ceil(root)
    row = math.floor(root)

    if row*col < length:
        row += 1

    grid = []
    index = 0

    for i in range(row):
        grid_row = []
        for j in range(col):
            if (index < length):
                grid_row.append(no_sp[index])
            else:
                grid_row.append("")
            index += 1
        grid.append(grid_row)

    result = ""

    for i in range(col):
        for j in range(row):
            result += grid[j][i]
        result += " "

    result = result[:-1]

    return result





print(encryption("chillout"))