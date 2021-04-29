def countingValleys(steps, path):
    # Write your code here
    valley_ctr = 0
    history = []
    current_level = 0

    index = 0

    for p in path:
        if p == 'D':
            current_level -= 1
        elif p == 'U':
            current_level += 1

        if current_level == -1:
            if index == 0:
                valley_ctr += 1
            elif len(history) > 1:
                if history[len(history) - 1] == 0:
                    valley_ctr += 1

        history.append(current_level)

        index += 1

    return valley_ctr


print(countingValleys(8, 'UDDDUDUU'))


