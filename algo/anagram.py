def is_anagram(s1, s2):
    if len(s1) != len(s2):
        return False

    checker = [0] * 256

    for letter in s1:
        checker[ord(letter)] = checker[ord(letter)] + 1

    anagram = True

    for letter in s2:
        if checker[ord(letter)] == 0:
            anagram = False
            break
        else:
            checker[ord(letter)] -= 1

    return anagram


print(is_anagram('Anikaaaa', 'akaainAa'))
