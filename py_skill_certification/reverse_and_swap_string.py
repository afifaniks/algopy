def reverse_words_order_and_swap_cases(sentence):
    split = sentence.split()

    res = ""
    for i in range(len(split) - 1, -1, -1):
        word = split[i]

        for letter in word:
            if letter >= 'a' and letter <= 'z':
                res += letter.upper()
            elif letter >= 'A' and letter <= 'Z':
                res += letter.lower()

        if i != 0:
            res += ' '

    return  res

print(reverse_words_order_and_swap_cases("aWESOME is cODING"))
