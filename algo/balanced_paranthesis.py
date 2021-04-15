from ds.stack import Stack


# Balanced parenthesis
string2 = "()()(())"
string3 = "((()()))()"

s = Stack()

for br in string3:
    if br == "(":
        s.push(br)
    elif br == ")":
        if s.size() != 0:
            if s.peek() == "(":
                s.pop()
            else:
                s.push(br)
        else:
            s.push(br)

if s.is_empty():
    print("Balanced")
else:
    print("Imbalanced")
