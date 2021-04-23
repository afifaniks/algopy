def convert(num, base):
    matches = "0123456789ABCDEF"
    if num < base:
        return matches[num]
    else:
        return convert(num//base, base) + matches[num%base]


print(convert(1453,16))
