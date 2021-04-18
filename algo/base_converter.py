from ds.stack import Stack


def convert(num, base):
    digits = "0123456789ABCDEF"
    stack = Stack()

    while num > 0:
        rem = num % base
        stack.push(rem)
        num = num // base

    bin = ""
    while not stack.is_empty():
        bin += str(digits[stack.pop()])

    print(bin)


convert(26, 26)
