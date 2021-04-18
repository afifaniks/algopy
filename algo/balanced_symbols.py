from ds.stack import Stack


def is_balanced(string):
    stack = Stack()

    for letter in string:
        if letter in "[{(":
            stack.push(letter)
        elif letter == ')' and stack.peek() == '(':
            stack.pop()
        elif letter == '}' and stack.peek() == '{':
            stack.pop()
        elif letter == ']' and stack.peek() == '[':
            stack.pop()
        else:
            stack.push(letter)

    if stack.is_empty():
        return True
    else:
        return False

str1 = "[]{}([{}]()"
str2 = "{({([][])}())}"
str3 = "[{()]"

print(is_balanced(str1))
print(is_balanced(str2))
print(is_balanced(str3))