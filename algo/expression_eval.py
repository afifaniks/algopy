from ds.stack import Stack

def convert_postfix(expr):
    """
    Converts an infix expression to postfix
    The function assumes each operand and operators
    are separated by whitespaces
    :param expr: infix expression
    :return: postfix expression
    """
    cleaned_expr = expr.split()
    opstack = Stack()
    output = []
    operators = {
        '+': 1,
        '-': 2,
        '*': 3,
        '/': 4,
        '(': 1,
        ')': 1
    }

    for op in cleaned_expr:
        if op in operators:
            if op == "(":
                opstack.push(op)
            elif op == ")":
                stack_peek = opstack.pop()
                while not opstack.is_empty() and stack_peek != "(":
                    output.append(stack_peek)
                    stack_peek = opstack.pop()

            elif not opstack.is_empty() and (operators[op] < operators[opstack.peek()]):
                stack_peek = opstack.pop()
                while not opstack.is_empty() and (operators[op] <= operators[opstack.peek()]):
                    output.append(stack_peek)
                    stack_peek = opstack.pop()
                output.append(stack_peek)
                opstack.push(op)
            else:
                opstack.push(op)
        else:
            output.append(op)

    while not opstack.is_empty():
        output.append(opstack.pop())

    return "".join(output)


# print(convert_postfix("A*B+C*D"))
print(convert_postfix("( A + B ) * C - ( D - E ) * ( F + G )"))
