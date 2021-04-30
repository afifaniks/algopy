def twoStrings(s1, s2):
    for s in s1:
        if s in s2:
            return "YES"
    return "NO"

print(twoStrings("wouldyoulikefries", "abcabcabcabcabcabc"))