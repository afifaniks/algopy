from ds.stack import Stack

s = Stack()

# Reverse string using stack
string = "Anik Mia"
for letter in string:
    s.push(letter)

rev = ""
while not s.is_empty():
    rev += s.pop()

print(rev)