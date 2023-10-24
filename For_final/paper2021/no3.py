'''
Define a recursive Python function count_operand_in_expr to return the number of
operands in an infix expression in which all operators are binary ones.
'''

def count_operands_in_expr(expr):
    if type(expr) != tuple:
        return 1
    else:
        return count_operands_in_expr(expr[0]) + count_operands_in_expr(expr[2])
    
print(count_operands_in_expr((3, "*", 2)))
print(count_operands_in_expr((4, "+", (3, "*", 2))))