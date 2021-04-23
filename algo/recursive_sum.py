def add_list(num_list):
    if len(num_list) == 1:
        return num_list[0]
    sum = num_list[0] + add_list(num_list[1:])

    return sum


print(add_list([1, 5, 4]))