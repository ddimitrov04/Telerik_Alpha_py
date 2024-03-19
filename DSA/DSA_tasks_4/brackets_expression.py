def extract_bracket_expressions(expression):
    stack = []
    expressions= []

    for i, char in enumerate(expression):
        if char == "(":
            stack.append(i)
        elif char == ")":
            start_ind = stack.pop()
            expressions.append(expression[start_ind:i+1])

    return expressions


expressionn = input()
all_new_expressions = extract_bracket_expressions(expressionn)
for expr in all_new_expressions:
    print(expr)
